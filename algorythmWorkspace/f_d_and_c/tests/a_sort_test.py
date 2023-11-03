import random
import unittest
import sys
from a_merge_sort import *
from b_quick_sort import *
sys.path.append(r'C:\AI-backend\TIL\algorythmWorkspace\f_d_and_c')
# python -m unittest -v tests.a_sort_test.SortTest.test_merge

class SortTest(unittest.TestCase):
    def test_merge(self):
        print(merge([1,5,7,13], [2,4,9,12,15]))

    def test_mergesort(self):
        arr = [round(random.randrange(1,1000)) for _ in range(1000)]
        print(mergesort2(arr))

    def test_quicksort(self):
        #arr = [round(random.randrange(1,1000)) for _ in range(1000)]
        arr = [15, 22, 13, 27, 12, 10, 20, 25]
        print()
        print(quicksort(arr,0,len(arr)-1))

if __name__ == '__main__':
    unittest.main()