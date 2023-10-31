import unittest
import sys
sys.path.append(r'C:\AI-backend\TIL\algorythmWorkspace\b_datastructure')
from b_hashtable import *
# python -m unittest -v tests.b_hashtable_test.HashTableTest.test_hash

class HashTableTest(unittest.TestCase):


    def setUp(self):
        self.table = HashTable()
        self.table.add("a", "안녕하세요1")
        self.table.add("b", "안녕하세요b")
        self.table.add("c", "안녕하세요c")
        self.table.add("d", "안녕하세요d")

    def test_hash(self):        
        print(self.table)

    def test_set(self):        
        table = HashTable()
        table.set("a", "안녕하세요1")
        table.set("a", "안녕하세요2")
        table.set("a", "안녕하세요3")
        table.set("d", "안녕하세요d")
        table.set("e", "안녕하세요e")
        table.set("f", "안녕하세요f")

        print(table)
        
    def test_get(self):        
        print(self.table.get("asdajksdb"))
    
    
    def test_iter(self):
        for e in self.table:
            print(e)


    

if __name__ == '__main__':
    unittest.main()