import unittest
import sys
sys.path.append(r'C:\AI-backend\TIL\algorythmWorkspace\a_basic')
from c_math import *
# 테스트 명령어 : python -m unittest -v tests.math_test.MathTest.test_fibonacci
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

    def test_fibonacci(self):
        self.assertEqual(fibonacci(10), 55)

    def test_fibo_recur(self):
        self.assertEqual(fibo_recur(10), 55)