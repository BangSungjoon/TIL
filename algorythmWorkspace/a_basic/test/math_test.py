import unittest
import sys
sys.path.append(r'C:\AI-backend\TIL\algorythmWorkspace\a_basic')
from c_math import *

class MathTest(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(324931))

    def test_prime3(self):
        self.assertTrue(is_prime(324931))

    def test_gcd(self):
        self.assertEqual(gcd1(12,18),6)

    def test_qcm(self):
        print(lcm(900000, 1680540))

    def test_factorial(self):
        self.assertEqual(factorial1(4), 24)

if __name__ == '__main__':
    unittest.main()