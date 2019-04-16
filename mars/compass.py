# -*- coding: utf-8 -*-


class Compass(object):
    N = 1
    E = 2
    S = 3
    W = 4

    def __init__(self, direction):
        self.state = getattr(self, direction)

    def left(self):
        self.state = self.W if self.state == self.N else (self.state - 1)

    def right(self):
        self.state = self.N if self.state == self.W else (self.state + 1)

    def __str__(self):
        return str(self.state)
