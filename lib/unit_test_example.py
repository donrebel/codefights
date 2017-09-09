import unittest
from solver import Solver


class MyTestCase(unittest.TestCase):

    def test_negative_discr(self):
        s = Solver()
        self.assertRaises(Exception, s.demo, 2, 1, 1)

    def test_dumy(self):
        s = Solver()
        self.assertEqual(2, s.ddumy(2, 1))

    def test_something(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
