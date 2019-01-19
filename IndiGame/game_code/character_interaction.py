class GetSide:
    def __init__(self, ob1=None, ob2=None, player=None, l=False, r=False):
        self.ob1 = ob1
        self.ob2 = ob2
        self.player = player
        self.l = l
        self.r = r


    def getting_side(self):
        ret_val = [0, 0, 0, 0]  # left right top bottom
        if self.ob2 is None and self.ob1 is not None and self.player is not None:
            if -32 <= (self.ob1.shell.top - self.player.player.bottom) <= 0 and (
                    self.ob1.shell.right > self.player.player.left and self.ob1.shell.left < self.player.player.right):
                ret_val[2] = 1

            if 32 >= (self.ob1.shell.bottom - self.player.player.top) >= 0 and (
                    self.ob1.shell.right > self.player.player.left and self.ob1.shell.left < self.player.player.right):
                ret_val[3] = 1
            if 32 >= (self.ob1.shell.right - self.player.player.left) >= 0 and self.l and (
                    self.ob1.shell.top < self.player.player.bottom and self.ob1.shell.bottom > self.player.player.top):
                ret_val[0] = 1

            if -32 <= (self.ob1.shell.left - self.player.player.right) <= 0 and self.r and (
                    self.ob1.shell.top < self.player.player.bottom and self.ob1.shell.bottom > self.player.player.top):
                ret_val[1] = 1

            return ret_val

        if self.ob1 is not None and self.ob2 is not None and self.player is None:
            if -16 <= (self.ob1.now_pos[1] - self.ob2.now_pos[1]-self.ob2.size[1]) <= 0 and (
                    self.ob1.now_pos[0]+self.ob1.size[0] > self.ob2.now_pos[0] and self.ob1.now_pos[0] < self.ob2.now_pos[0]+self.ob2.size[0]):
                ret_val[2] = 1

            if 16 >= (self.ob1.now_pos[1] + self.ob1.size[1] - self.ob2.now_pos[1]) >= 0 and (
                    self.ob1.now_pos[0]+self.ob1.size[0] > self.ob2.now_pos[0] and self.ob1.now_pos[0] < self.ob2.now_pos[0]+self.ob2.size[0]):
                ret_val[3] = 1

            if 16 >= (self.ob1.now_pos[0]+self.ob1.size[0] - self.ob2.now_pos[0]) >= 0 and self.l and (
                    self.ob1.now_pos[1] < self.ob2.now_pos[1]+self.ob2.size[1] and self.ob1.now_pos[1] + self.ob1.size[1] > self.ob2.now_pos[1]):
                ret_val[0] = 1

            if -16 <= (self.ob1.now_pos[0] - self.ob2.now_pos[0]-self.ob2.size[0]) <= 0 and self.r and (
                    self.ob1.now_pos[1] < self.ob2.now_pos[1]+self.ob2.size[1] and self.ob1.now_pos[1] + self.ob1.size[1] > self.ob2.now_pos[1]):
                ret_val[1] = 1

            return ret_val

class ObjIsNear:
    def __init__(self, ob1=None, ob2=None, player=None):
        self.ob1 = ob1
        self.ob2 = ob2
        self.player = player

    def getting_side(self):
        ret_val = [0, 0, 0, 0]  # left right top bottom

        if self.ob2 is None and self.ob1 is not None and self.player is not None:
            if 128 >= (self.ob1.shell.top - self.player.player.bottom) >= -128 and (
                    self.ob1.shell.right > self.player.player.left and self.ob1.shell.left < self.player.player.right):
                ret_val[2] = 1

            if -128 <= (self.ob1.shell.bottom - self.player.player.top) <= 128 and (
                    self.ob1.shell.right > self.player.player.left and self.ob1.shell.left < self.player.player.right):
                ret_val[3] = 1
            if -128 <= (self.ob1.shell.right - self.player.player.left) <= 128 and (
                    self.ob1.shell.top < self.player.player.bottom and self.ob1.shell.bottom > self.player.player.top):
                ret_val[0] = 1

            if 128 >= (self.ob1.shell.left - self.player.player.right) >= -128 and (
                    self.ob1.shell.top < self.player.player.bottom and self.ob1.shell.bottom > self.player.player.top):
                ret_val[1] = 1

            return ret_val

        if self.ob1 is not None and self.ob2 is not None and self.player is None:
            if 32 >= (self.ob1.now_pos[1] - self.ob2.now_pos[1] - self.ob2.size[1]) >= 0 and (
                    self.ob1.now_pos[0] + self.ob1.size[0] > self.ob2.now_pos[0] and
                    self.ob1.now_pos[0] < self.ob2.now_pos[0] + self.ob2.size[0]):
                ret_val[2] = 1

            if -32 <= (self.ob1.now_pos[1] + self.ob1.size[1] - self.ob2.now_pos[1]) <= 0 and (
                    self.ob1.now_pos[0] + self.ob1.size[0] > self.ob2.now_pos[0] and
                    self.ob1.now_pos[0] < self.ob2.now_pos[0] + self.ob2.size[0]):
                ret_val[3] = 1

            if -32 <= (self.ob1.now_pos[0] + self.ob1.size[0] - self.ob2.now_pos[
                0]) <= 0 and (
                    self.ob1.now_pos[1] < self.ob2.now_pos[1] + self.ob2.size[1] and
                    self.ob1.now_pos[1] + self.ob1.size[1] > self.ob2.now_pos[1]):
                ret_val[0] = 1

            if 32 >= (self.ob1.now_pos[0] - self.ob2.now_pos[0] - self.ob2.size[
                0]) >= 0 and (
                    self.ob1.now_pos[1] < self.ob2.now_pos[1] + self.ob2.size[1] and
                    self.ob1.now_pos[1] + self.ob1.size[1] > self.ob2.now_pos[1]):
                ret_val[1] = 1
            return ret_val