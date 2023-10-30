import unittest
import sys
sys.path.append(r'C:\CODE\mc_2023_algorythm\b_datastructure')
from a_list import LinkedList

class ListTest(unittest.TestCase):       
    def setUp(self):
        self.list = LinkedList()
        self.list.append("data")
        self.list.append("structure")
        self.list.append(100)
        self.list.append(True)
    
    def test_str(self):        
        print(self.list)   
        
    def test_pop(self):      
        print(self.list.pop())
        print(self.list)
        
    def test_getitem(self):       
        print(self.list.get(0))
        print(self.list)
        
    def test_setitem(self):     
        self.list[1] = 100
        print(self.list)
  
    def test_delitem(self):     
        del(self.list[100])
        print(self.list)
        
    def test_insert(self):     
        self.list.insert(3,"2번")
        print(self.list)
        
    def test_iter(self):     
        for e in self.list:
            print(e)
    
    
if __name__ == '__main__':
    unittest.main()