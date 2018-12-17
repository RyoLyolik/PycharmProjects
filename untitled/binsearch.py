from math import sqrt
class binsearch:
    def __init__(self, a, l, r, val):
        self.a = a
        self.l = l
        self.r = r
        self.val = val
    def upbound(self): # upper bound
        while self.r - self.l > 1:
            m = (self.l + self.r) // 2
            if self.a[m] <= self.val:
                self.l = m
            else:
                self.r = m
        return self.l
    def lowbound(self): # lower bound
        while self.r != self.l:
            self.m = (self.l + self.r) // 2
            if self.a[m] < val:
                self.l = m + 1
            else:
                self.r = m
        return self.l


