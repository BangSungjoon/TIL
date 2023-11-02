import unittest
import sys
sys.path.append(r'C:\AI-backend\TIL\algorythmWorkspace\b_datastructure')
from e_bst import *
# python -m unittest -v tests.b_hashtable_test.HashTableTest.test_hash

class BSTTest(unittest.TestCase):
    def test_dfs(self):
        bst = BinarySearchTree()
        for i in [8,3,10,1,6,14,4,7,13]:
            bst.insert(i)

        print('preorder', bst.pre_order_stack())
        print('inorder:', bst.in_order_stack2())
        print('postorder:', bst.post_order_stack())

if __name__ == '__main__':
    unittest.main()