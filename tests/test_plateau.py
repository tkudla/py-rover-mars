import unittest

from mars.compass import Compass
from mars.exceptions import NasaException
from mars.plateau import Plateau
from mars.rover import Rover


class TestPlateau(unittest.TestCase):

    def setUp(self):
        super(TestPlateau, self).setUp()

        self.rover_default = {"x": 0, "y": 0, "direction": "N"}
        self.plateau_default = {"upper_x": 5, "upper_y": 5}

    def test_generic(self):
        """
        Generic test for:

        Test Input:
        5 5
        1 2 N
        LMLMLMLMM
        3 3 E
        MMRMMRMRRM

        Expected Output:
        1 3 N
        5 1 E
        """
        plateau = Plateau(**self.plateau_default)

        rover1 = Rover(**{"x": 1, "y": 2, "direction": "N"})
        plateau.accept(rover1)
        plateau.move(rover1, "LMLMLMLMM")

        self.assertTrue(rover1.state().endswith("1 3 N"))
        self.assertEqual(rover1.position_x, 1)
        self.assertEqual(rover1.position_y, 3)
        self.assertEqual(rover1.compass.state, Compass.N)

        rover2 = Rover(**{"x": 3, "y": 3, "direction": "E"})
        plateau.accept(rover2)
        plateau.move(rover2, "MMRMMRMRRM")

        self.assertTrue(rover2.state().endswith("5 1 E"))
        self.assertEqual(rover2.position_x, 5)
        self.assertEqual(rover2.position_y, 1)
        self.assertEqual(rover2.compass.state, Compass.E)

    def test_accept_valid(self):
        """
        Tests landing OK
        """
        plateau = Plateau(**self.plateau_default)
        rover = Rover(**self.rover_default)
        plateau.accept(rover)
        self.assertIn(rover, plateau.rovers)

    def test_accept_outside(self):
        """
        Tests rover lands outside the plateau
        """
        plateau = Plateau(**self.plateau_default)
        rover = Rover(**self.rover_default)

        rover.command("M" * 10)

        with self.assertRaises(NasaException):
            plateau.accept(rover)

    def test_cell_taken(self):
        """
        Tests if plateau cell taken
        """
        plateau = Plateau(**self.plateau_default)
        rover1 = Rover(**self.rover_default)
        rover2 = Rover(**{"x": 1, "y": 1, "direction": "N"})

        plateau.accept(rover1)
        plateau.accept(rover2)

        with self.assertRaises(NasaException):
            plateau.move(rover1, "MRM")

    def test_move_ok(self):
        """
        Tests rover plateau move was ok
        """
        plateau = Plateau(**self.plateau_default)
        rover = Rover(**self.rover_default)

        plateau.move(rover, "RMM")
        plateau.check_move(rover)

    def test_move_outside(self):
        """
        Tests rover move outside plateau
        """
        plateau = Plateau(**self.plateau_default)
        rover = Rover(**self.rover_default)

        self.assertEqual(rover.position_x, 0)
        self.assertEqual(rover.position_y, 0)

        with self.assertRaises(NasaException):
            plateau.move(rover, "LMMMMM")
