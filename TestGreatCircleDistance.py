import unittest
from GreatCircle import great_circle

THRESHOLD = .0001


class BasicGreatCircle(unittest.TestCase):

    def test_get_distance_known_distance(self):
        a = (51.886057, -8.404892)
        b = (51.867386, -8.472192)
        self.assertEqual(7.760090644929735, great_circle(*a, *b))

    def test_get_distance_basic(self):
        a = (0, 0)
        b = (1, 1)
        self.assertEqual(157.2493812719255, great_circle(*a, *b))


if __name__ == '__main__':
    unittest.main()
