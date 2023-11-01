import unittest
import sys
sys.path.append(r'C:\AI-backend\TIL\algorythmWorkspace\b_datastructure')
from d_queue_q import *
# python -m unittest -v tests.b_hashtable_test.HashTableTest.test_hash

class QueueQTest(unittest.TestCase):
    def test_q1(self):
        print(q1(4))

if __name__ == '__main__':
    unittest.main()