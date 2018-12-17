from pyglet.gl import *
from pyglet.window import key,mouse
from collections import deque
import sys, os, time, math, random


class Model:

    alpha_textures = 'leaves_oak','tall_grass'

    def load_textures(self):
        t = self.texture = {}; self.texture_dir = {}; dirs = ['textures']
        while dirs:
            dir = dirs.pop(0); textures = os.listdir(dir)
            for file in textures:
                if os.path.isdir(dir+'/'+file): dirs+=[dir+'/'+file]
                else:
                    n = file.split('.')[0]; self.texture_dir[n] = dir; image = pyglet.image.load(dir+'/'+file)
                    transparent = n in self.alpha_textures
                    texture = image.texture if transparent else image.get_mipmapped_texture()
                    self.texture[n] = pyglet.graphics.TextureGroup(texture)
                    if not transparent: glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST_MIPMAP_LINEAR)
                    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)

        self.block = {}; self.ids = []; done = []
        items = sorted(self.texture_dir.items(),key=lambda i:i[0])
        for name,dir in items:
            n = name.split(' ')[0]
            if n in done: continue
            done+=[n]
            if dir.startswith('textures/blocks'):
                self.ids+=[n]
                if dir=='textures/blocks': self.block[n] = t[n],t[n],t[n],t[n],t[n],t[n]
                elif dir=='textures/blocks/tbs': self.block[n] = t[n+' s'],t[n+' s'],t[n+' b'],t[n+' t'],t[n+' s'],t[n+' s']
                elif dir=='textures/blocks/ts': self.block[n] = t[n+' s'],t[n+' s'],t[n+' t'],t[n+' t'],t[n+' s'],t[n+' s']

        self.ids+=['water']
        flow,still = t['water_flow'],t['water_still']
        self.block['water'] = flow,flow,still,still,flow,flow

    def draw(self):
        glEnable(GL_ALPHA_TEST); self.opaque.draw(); glDisable(GL_ALPHA_TEST)
        glColorMask(GL_FALSE,GL_FALSE,GL_FALSE,GL_FALSE); self.transparent.draw()
        glColorMask(GL_TRUE,GL_TRUE,GL_TRUE,GL_TRUE); self.transparent.draw()

    def update(self,dt):
        self.cubes.water.update(dt)

    def __init__(self):
        self.opaque = pyglet.graphics.Batch()
        self.transparent = pyglet.graphics.Batch()
        self.load_textures()
        self.cubes = CubeHandler(self)

        for x in range(-16,16):
            for z in range(-16,16):
                self.cubes.add((x,-2,-z),'water')
                self.cubes.add((x,-3,-z),'water')
                self.cubes.add((x,-4,-z),'leaves_oak')
                self.cubes.add((x,-5,-z),'log_oak')

        for cube in self.cubes.cubes.values(): self.cubes.update_cube(cube)






class Water:
    def __init__(self,transparent):
        self.transparent = transparent
        self.time = {'still':TimeLoop(32),'flow':TimeLoop(32)}
        self.coords = {'still':[],'flow':[]}; self.still_faces = {}; self.flow_faces = {}
        for i in range(32-1,-1,-1):
            y0 = i/16; y1 = (i+1)/16; self.coords['still'] += [[0,y0, 1,y0, 1,y1, 0,y1]]
            y0 = i/32; y1 = (i+1)/32; self.coords['flow'] += [[0,y0, 1,y0, 1,y1, 0,y1]]
        a,b = self.time['still'],self.time['flow']; self.t = b,b,a,a,b,b
        a,b = self.coords['still'],self.coords['flow']; self.c = b,b,a,a,b,b

    def update(self,dt):
        if self.time['still'].update(dt*0.5):
            for face,i in self.still_faces.items(): face.tex_coords = self.c[i][self.t[i].int]
        if self.time['flow'].update(dt):
            for face,i in self.flow_faces.items(): face.tex_coords = self.c[i][self.t[i].int]

    def show(self,v,t,i):
        face = self.transparent.add(4,GL_QUADS,t,('v3f',v),('t2f',self.c[i][0]))
        faces = self.still_faces if i==2 or i==3 else self.flow_faces
        faces[face] = i; return face




class CubeHandler:
    def __init__(self,model):
        self.model = model
        self.opaque,self.transparent = model.opaque,model.transparent
        self.block,self.alpha_textures = model.block,model.alpha_textures
        self.water = Water(self.transparent)
        self.cubes = {}

    def hit_test(self,p,vec,dist=256):
        if normalize(p) in self.cubes: return None,None
        m = 8; x,y,z = p; dx,dy,dz = vec
        dx/=m; dy/=m; dz/=m; prev = None
        for i in range(dist*m):
            key = normalize((x,y,z))
            if key in self.cubes: return key,prev
            prev = key
            x,y,z = x+dx,y+dy,z+dz
        return None,None

    def show(self,v,t,i): return self.opaque.add(4,GL_QUADS,t,('v3f',v),('t2f',(0,0, 1,0, 1,1, 0,1)))

    def update_cube(self,cube):
        if not any(cube.shown.values()): return
        show = self.water.show if cube.name=='water' else self.show
        v = cube_vertices(cube.p)
        f = 'left','right','bottom','top','back','front'
        for i in (0,1,2,3,4,5):
            if cube.shown[f[i]] and not cube.faces[f[i]]: cube.faces[f[i]] = show(v[i],cube.t[i],i)

    def set_adj(self,cube,adj,state):
        x,y,z = cube.p; X,Y,Z = adj; d = X-x,Y-y,Z-z; f = 'left','right','bottom','top','back','front'
        for i in (0,1,2):
            if d[i]:
                j = i+i; a,b = [f[j+1],f[j]][::d[i]]; cube.shown[a] = state
                if not state and cube.faces[a]: cube.faces[a].delete(); face = cube.faces[a]; cube.faces[a] = None; self.remove_water(face)

    def add(self,p,t,now=False):
        if p in self.cubes: return
        cube = self.cubes[p] = Cube(t,p,self.block[t],'alpha' if t in self.alpha_textures else 'blend' if t=='water' else 'solid')

        for adj in adjacent(*cube.p):
            if adj not in self.cubes: self.set_adj(cube,adj,True)
            else:
                a,b = cube.type,self.cubes[adj].type
                if a==b and (a=='solid' or b=='blend'): self.set_adj(self.cubes[adj],cube.p,False)
                elif a!='blend' and b!='solid': self.set_adj(self.cubes[adj],cube.p,False); self.set_adj(cube,adj,True)

        if now: self.update_cube(cube)

    def remove_water(self,face):
        if face in self.water.still_faces: del self.water.still_faces[face]
        elif face in self.water.flow_faces: del self.water.flow_faces[face]

    def remove(self,p):
        if p not in self.cubes: return
        cube = self.cubes.pop(p)

        for side,face in cube.faces.items():
            if face: face.delete()
            self.remove_water(face)

        for adj in adjacent(*cube.p):
            if adj in self.cubes:
                self.set_adj(self.cubes[adj],cube.p,True)
                self.update_cube(self.cubes[adj])



class Cube:
    def __init__(self,name,p,t,typ):
        self.name,self.p,self.t,self.type = name,p,t,typ
        self.shown = {'left':False,'right':False,'bottom':False,'top':False,'back':False,'front':False}
        self.faces = {'left':None,'right':None,'bottom':None,'top':None,'back':None,'front':None}

class TimeLoop:
    def __init__(self,duration): self.unit = 0; self.int = 0; self.duration = duration; self.prev = 0
    def update(self,dt):
        self.unit+=dt; self.unit-=int(self.unit); self.int = int(self.unit*self.duration)
        if self.prev!=self.int: self.prev = self.int; return True

def cube_vertices(pos,n=0.5):
    x,y,z = pos; v = tuple((x+X,y+Y,z+Z) for X in (-n,n) for Y in (-n,n) for Z in (-n,n))
    return tuple(tuple(k for j in i for k in v[j]) for i in ((0,1,3,2),(5,4,6,7),(0,4,5,1),(3,7,6,2),(4,0,2,6),(1,5,7,3)))

def flatten(lst): return sum(map(list,lst),[])
def normalize(pos): x,y,z = pos; return round(x),round(y),round(z)

def adjacent(x,y,z):
    for p in ((x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z),(x,y,z-1),(x,y,z+1)): yield p


class Player:

    WALKING_SPEED = 5
    FLYING_SPEED = 15

    GRAVITY = 20
    JUMP_SPEED = (2*GRAVITY)**.5
    TERMINAL_VELOCITY = 50

    def push(self): glPushMatrix(); glRotatef(-self.rot[0],1,0,0); glRotatef(self.rot[1],0,1,0); glTranslatef(-self.pos[0],-self.pos[1],-self.pos[2])

    def __init__(self,cubes,pos=(0,0,0),rot=(0,0)):
        self.cubes = cubes
        self.pos,self.rot = list(pos),list(rot)
        self.flying = False
        self.noclip = False
        self.dy = 0

    def mouse_motion(self,dx,dy):
        dx/=8; dy/=8; self.rot[0]+=dy; self.rot[1]+=dx
        if self.rot[0]>90: self.rot[0] = 90
        elif self.rot[0]<-90: self.rot[0] = -90

    def jump(self):
        if not self.dy: self.dy = self.JUMP_SPEED

    def get_sight_vector(self):
        rotX,rotY = self.rot[0]/180*math.pi,self.rot[1]/180*math.pi
        dx,dz = math.sin(rotY),-math.cos(rotY)
        dy,m = math.sin(rotX),math.cos(rotX)
        return dx*m,dy,dz*m

    def update(self,dt,keys):
        DX,DY,DZ = 0,0,0; s = dt*self.FLYING_SPEED if self.flying else dt*self.WALKING_SPEED
        rotY = self.rot[1]/180*math.pi
        dx,dz = s*math.sin(rotY),s*math.cos(rotY)
        if self.flying:
            if keys[key.LSHIFT]: DY-=s
            if keys[key.SPACE]: DY+=s
        elif keys[key.SPACE]: self.jump()
        if keys[key.W]: DX+=dx; DZ-=dz
        if keys[key.S]: DX-=dx; DZ+=dz
        if keys[key.A]: DX-=dz; DZ-=dx
        if keys[key.D]: DX+=dz; DZ+=dx

        if dt<0.2:
            dt/=10; DX/=10; DY/=10; DZ/=10
            for i in range(10): self.move(dt,DX,DY,DZ)

    def move(self,dt,dx,dy,dz):
        if not self.flying:
            self.dy -= dt*self.GRAVITY
            self.dy = max(self.dy,-self.TERMINAL_VELOCITY)
            dy += self.dy*dt

        x,y,z = self.pos
        self.pos = self.collide((x+dx,y+dy,z+dz))

    def collide(self,pos):
        if self.noclip and self.flying: return pos
        pad = 0.25; p = list(pos); np = normalize(pos)
        for face in ((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)):
            for i in (0,1,2):
                if not face[i]: continue
                d = (p[i]-np[i])*face[i]
                if d<pad: continue
                for dy in (0,1):
                    op = list(np); op[1]-=dy; op[i]+=face[i]; op = tuple(op)
                    if op in self.cubes:
                        p[i]-=(d-pad)*face[i]
                        if face[1]: self.dy = 0
                        break
        return tuple(p)




class Window(pyglet.window.Window):

    def set2d(self): glMatrixMode(GL_PROJECTION); glLoadIdentity(); gluOrtho2D(0,self.width,0,self.height)
    def set3d(self): glLoadIdentity(); gluPerspective(65,self.width/self.height,0.1,320); glMatrixMode(GL_MODELVIEW); glLoadIdentity()
    def on_resize(self,w,h): glViewport(0,0,w,h); self.load_vertex_lists(w,h)
    def setLock(self,state): self.set_exclusive_mouse(state); self.mouseLock = state
    mouseLock = False; mouse_lock = property(lambda self:self.mouseLock,setLock)

    def __init__(self,*args):
        super().__init__(*args)
        pyglet.clock.schedule(self.update)
        self.keys = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keys)
        self.model = Model()
        self.player = Player(self.model.cubes.cubes)
        self.mouse_lock = True
        self.fps = pyglet.clock.ClockDisplay()
        self.reticle = None
        self.block = 0

    def load_vertex_lists(self,w,h):
        x,y = w/2,h/2; m = 10
        if self.reticle: self.reticle.delete()
        self.reticle = pyglet.graphics.vertex_list(4,('v2f',(x-m,y, x+m,y, x,y-m, x,y+m)),('c3f',(0,0,0, 0,0,0, 0,0,0, 0,0,0)))
        self.water = pyglet.graphics.vertex_list(4,('v2f',(0,0, w,0, w,h, 0,h)),('c4f',[0.15,0.3,1,0.5]*4))

    def update(self,dt):
        self.player.update(dt,self.keys)
        self.model.update(dt)

    def on_mouse_motion(self,x,y,dx,dy):
        if self.mouse_lock: self.player.mouse_motion(dx,dy)

    def on_mouse_press(self,x,y,button,MOD):
        if button == mouse.LEFT:
            block = self.model.cubes.hit_test(self.player.pos,self.player.get_sight_vector())[0]
            if block: self.model.cubes.remove(block)
        elif button == mouse.RIGHT:
            block = self.model.cubes.hit_test(self.player.pos,self.player.get_sight_vector())[1]
            if block: self.model.cubes.add(block,self.model.ids[self.block],True)

    def on_key_press(self,KEY,MOD):
        if KEY == key.ESCAPE: self.dispatch_event('on_close')
        elif KEY == key.E: self.mouse_lock = not self.mouse_lock
        elif KEY == key.F: self.player.flying = not self.player.flying; self.player.dy = 0; self.player.noclip = True
        elif KEY == key.C: self.player.noclip = not self.player.noclip
        elif KEY == key.UP: self.block = (self.block-1)%len(self.model.ids)
        elif KEY == key.DOWN: self.block = (self.block+1)%len(self.model.ids)

    def on_draw(self):
        self.clear()
        self.set3d()
        self.player.push()
        self.model.draw()

        block = self.model.cubes.hit_test(self.player.pos,self.player.get_sight_vector())[0]
        if block:
            glPolygonMode(GL_FRONT_AND_BACK,GL_LINE); glColor3d(0,0,0)
            pyglet.graphics.draw(24,GL_QUADS,('v3f/static',flatten(cube_vertices(block,0.52))))
            glPolygonMode(GL_FRONT_AND_BACK,GL_FILL); glColor3d(1,1,1)

        glPopMatrix()
        self.set2d()

        cubes = self.model.cubes.cubes; p = normalize(self.player.pos)
        if p in cubes and cubes[p].name=='water': self.water.draw(GL_POLYGON)

        self.fps.draw()
        self.reticle.draw(GL_LINES)



def main():
    window = Window(800,600,'Minecraft',True)
    glClearColor(0.5,0.7,1,1)
    glEnable(GL_DEPTH_TEST); glDepthFunc(GL_LEQUAL); glAlphaFunc(GL_GEQUAL,1)
    glEnable(GL_BLEND); glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
    pyglet.app.run()


if __name__ == '__main__':
    main()
