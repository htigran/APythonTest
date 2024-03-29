import unittest
from GreatCircle import great_circle

THRESHOLD = .0001


class BasicGreatCircle(unittest.TestCase):

    def test_get_distance_known_distance(self):
        a = (51.886057, -8.404892)
        b = (51.867386, -8.472192)
        self.assertEqual(7.760090644929735, great_circle(*a, *b))
        home = (40.152635, 44.511932)
        dublin = (53.339428, -6.257664)
        wow = great_circle(*home, *dublin)
        self.assertEqual(5797.583869055684, wow)

    def test_get_distance_basic(self):
        a = (0, 0)
        b = (0, 0)
        self.assertEqual(0.0, great_circle(*a, *b))
        a = (53, 53)
        b = (53, 53)
        self.assertEqual(0.0, great_circle(*a, *b))

    """
    TODO: I should really have loads of edge cases 
    """

if __name__ == '__main__':
    unittest.main()
