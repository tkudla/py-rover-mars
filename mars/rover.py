# -*- coding: utf-8 -*-

from .compass import Compass


class Rover(object):
    RE_POSITION = r"(?P<x>\d+)\s(?P<y>\d+)\s(?P<direction>[NESW])"

    def __init__(self, x, y, direction):

        self.position_x = int(x)
        self.position_y = int(y)

        self.compass = Compass(direction)

    def command(self, cmd):

        for char in cmd:

            if char == "L":
                self.compass.left()

            elif char == "R":
                self.compass.right()

            elif char == "M":
                self.move()

    def move(self):

        direction = self.compass.state

        if direction == Compass.N:
            self.position_y += 1

        if direction == Compass.S:
            self.position_y -= 1

        if direction == Compass.E:
            self.position_x += 1

        if direction == Compass.W:
            self.position_x -= 1

    def state(self):
        return "<<< {} {} {}".format(self.position_x, self.position_y, self.compass)
