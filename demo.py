# -*- coding: utf-8 -*-

from __future__ import print_function

import re
import sys

from mars.exceptions import NasaException
from mars.plateau import Plateau
from mars.rover import Rover

if sys.version_info.major == 2:
    input = raw_input


def quite(regex=None):
    """
    Service method for console input
    """
    val = input('>>> ')

    if not val:
        sys.exit(0)

    try:
        if regex:
            return re.match(regex, val).groupdict()

    except (AttributeError, re.error):
        raise NasaException("NASA doesn't understand human language...")

    return val


if __name__ == "__main__":

    try:

        size = quite(Plateau.RE_SIZE)
        plateau = Plateau(**size)

        while True:
            position = quite(Rover.RE_POSITION)
            rover = Rover(**position)

            plateau.accept(rover)
            plateau.move(rover, quite())

            print(rover.state(), file=sys.stdout)

    except NasaException as e:
        print("Ops, {}".format(e), file=sys.stderr)
        sys.exit(1)
