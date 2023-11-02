import random
import unittest
import sys
from b_selection_sort import *
sys.path.append(r'C:\AI-backend\TIL\algorythmWorkspace\e_bruteforce')
from a_bubble_sort import *
# python -m unittest -v tests.b_hashtable_test.HashTableTest.test_hash

class SortTest(unittest.TestCase):
    def test_bubble_sort(self):
        arr = [round(random.randrange(1,1000)) for _ in range(1000)]
        print(bubble_sort(arr))

    def test_selection_sort(self):
        arr = [round(random.randrange(1,1000)) for _ in range(1000)]
        print(selection_sort(arr))

if __name__ == '__main__':
    unittest.main()