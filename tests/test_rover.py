import unittest

from mars.compass import Compass
from mars.rover import Rover


class TestRover(unittest.TestCase):
    initial = {"x": 1, "y": 1, "direction": "N"}

    def test_move(self):
        """
        Tests rover move
        """
        rover = Rover(**self.initial)
        rover.move()

        self.assertEqual(rover.position_x, 1)
        self.assertEqual(rover.position_y, 2)

        rover.command("LMRM")

        self.assertEqual(rover.position_x, 0)
        self.assertEqual(rover.position_y, 3)

    def test_command(self):
        """
        Tests rover command
        """
        rover = Rover(**self.initial)
        rover.command("LRLR")

        self.assertEqual(rover.position_x, self.initial.get("x"))
        self.assertEqual(rover.position_y, self.initial.get("y"))
        self.assertEqual(rover.compass.state, Compass.N)

    def test_state(self):
        """
        Tests valid state: x y direction
        """
        rover = Rover(**self.initial)
        rover.command("LLLLM")

        self.assertTrue(rover.state().endswith("1 2 N"), rover.state())
