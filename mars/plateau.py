# -*- coding: utf-8 -*-

from .exceptions import NasaException


class Plateau(object):
    lower_x = 0
    lower_y = 0

    RE_SIZE = r'(?P<upper_x>\d+)\s(?P<upper_y>\d+)'

    def __init__(self, upper_x, upper_y):

        self.rovers = []
        self.upper_x = int(upper_x)
        self.upper_y = int(upper_y)

    def move(self, rover, where):
        """
        Moves rover on plateau
        """
        rover.command(where)
        self.check_move(rover)

    def accept(self, rover):
        """
        Accepts rover to rovers list
        """
        self.check_move(rover)
        self.rovers.append(rover)

    def check_move(self, rover):
        """
        Checks rover's move, if outside plateau or another rover is there
        """
        if rover.position_x > self.upper_x or rover.position_x < self.lower_x \
                or rover.position_y > self.upper_y or rover.position_y < self.lower_y:
            raise NasaException("Rover landed outside the plateau and is now lost in space")

        for another in self.rovers:
            if another.position_x == rover.position_x and another.position_y == rover.position_y \
                    and id(rover) != id(another):
                raise NasaException("Another rover is sitting there")
