# -*- coding: utf-8 -*-


class Compass(object):
    N = 1
    E = 2
    S = 3
    W = 4

    def __init__(self, direction):
        self.state = getattr(self, direction)

    def left(self):
        """
        Moves to left
        """
        self.state = self.W if self.state == self.N else (self.state - 1)

    def right(self):
        """
        Moves to right
        """
        self.state = self.N if self.state == self.W else (self.state + 1)

    def get_direction(self):
        """
        Gets current state, N E S W
        """
        return {v: k for k, v in self.__class__.__dict__.items()}.get(self.state)

    def __str__(self):
        return self.get_direction()
