import unittest
import sys
sys.path.append(r'C:\AI-backend\TIL\algorythmWorkspace\b_datastructure')
from b_hashtable_q import *
# python -m unittest -v tests.b_hashtable_test.HashTableTest.test_hash

class HashTableTest(unittest.TestCase):
    def test_q1(self):        
        texts = ['hashtable', 'samsung', 'aabb']
        for text in texts:
            print(q1(text))
    

if __name__ == '__main__':
    unittest.main()