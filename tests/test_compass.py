import unittest

from mars.compass import Compass


class TestCompass(unittest.TestCase):

    def test_left(self):
        """
        Tests compass left move
        """
        compass = Compass('N')
        compass.left()
        self.assertEqual(compass.state, Compass.W)

        compass = Compass('W')
        compass.left()
        self.assertEqual(compass.state, Compass.S)

    def test_right(self):
        """
        Tests compass right move
        """
        compass = Compass('N')
        compass.right()
        self.assertEqual(compass.state, Compass.E)

        compass = Compass('S')
        compass.right()
        self.assertEqual(compass.state, Compass.W)

    def test_state(self):
        """
        Tests compass direction read
        """
        direction = 'N'
        self.assertEqual(Compass(direction).get_direction(), direction)
