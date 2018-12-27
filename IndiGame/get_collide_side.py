import pygame


class GetSide:
    def __init__(self, ob1=None, ob2=None, player=None, l=False, r=False):
        self.ob1 = ob1
        self.ob2 = ob2
        self.player = player
        self.l = l
        self.r = r

    def getting_side(self):
        # print(self.ob1,self.ob2,self.player)
        if self.ob2 is None and self.ob1 is not None and self.player is not None:
            # print(-32 < (self.ob1.shell.left - self.player.player.right) <= 0,self.r)
            if -32 > (self.ob1.shell.left - self.player.player.right) >= 0 and self.r:
                print('returned')
                return (0,1,0,0)
            else:
                return (0,0,0,0)