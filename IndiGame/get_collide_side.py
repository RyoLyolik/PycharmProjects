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
            if -32 <= (self.ob1.shell.top - self.ob2.shell.bottom) <= 0 and (
                    self.ob1.shell.right > self.ob2.shell.left and self.ob1.shell.left < self.ob2.shell.right):
                ret_val[2] = 1

            if 32 >= (self.ob1.shell.bottom - self.ob2.shell.top) >= 0 and (
                    self.ob1.shell.right > self.ob2.shell.left and self.ob1.shell.left < self.ob2.shell.right):
                ret_val[3] = 1
            if 32 >= (self.ob1.shell.right - self.ob2.shell.left) >= 0 and self.l and (
                    self.ob1.shell.top < self.ob2.shell.bottom and self.ob1.shell.bottom > self.ob2.shell.top):
                ret_val[0] = 1

            if -32 <= (self.ob1.shell.left - self.ob2.shell.right) <= 0 and self.r and (
                    self.ob1.shell.top < self.ob2.shell.bottom and self.ob1.shell.bottom > self.ob2.shell.top):
                ret_val[1] = 1
            return ret_val
