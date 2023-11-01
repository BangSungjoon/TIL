import unittest
import sys
sys.path.append(r'C:\AI-backend\TIL\algorythmWorkspace\b_datastructure')
from c_stack import *
# python -m unittest -v tests.b_hashtable_test.HashTableTest.test_hash

class StackTest(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)

        print(stack)

    def test_pop(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)

        for i in range(10):
            print(stack.pop(), end=' ')
        
        print(stack)

    def test_peak(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)

        for i in range(10):
            print(stack.peak(), end=' ')
        
        print(stack)

if __name__ == '__main__':
    unittest.main()