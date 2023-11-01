import unittest
import sys
sys.path.append(r'C:\AI-backend\TIL\algorythmWorkspace\b_datastructure')
from c_stack_q import *
# python -m unittest -v tests.b_hashtable_test.HashTableTest.test_hash

class StackQTest(unittest.TestCase):
    def test_q1(self):
        self.assertTrue(is_pair('{}()[]'))  # True
        self.assertTrue(is_pair('{([])}'))  # True
        self.assertFalse(is_pair('{([}])}')) # False

if __name__ == '__main__':
    unittest.main()