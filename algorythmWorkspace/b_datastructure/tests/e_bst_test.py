import unittest
import sys
sys.path.append(r'C:\AI-backend\TIL\algorythmWorkspace\b_datastructure')
from e_bst import *
# python -m unittest -v tests.b_hashtable_test.HashTableTest.test_hash

class BSTTest(unittest.TestCase):
    def test_pre_order(self):
        bst = BinarySearchTree()
        for i in [8,3,10,1,6,14,4,7,13]:
            bst.insert(i)

        print('preorder', bst.pre_order(bst.root))

if __name__ == '__main__':
    unittest.main()