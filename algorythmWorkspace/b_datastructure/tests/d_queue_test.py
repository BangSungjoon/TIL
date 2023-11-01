import unittest
import sys
sys.path.append(r'C:\AI-backend\TIL\algorythmWorkspace\b_datastructure')
from d_queue import *
# python -m unittest -v tests.b_hashtable_test.HashTableTest.test_hash

class QueueTest(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        for i in range(10):
            queue.enqueue(i)
        
        print(queue)

    def test_dequeue(self):
        queue = Queue()
        for i in range(10):
            queue.enqueue(i)

        for i in range(10):
            print(queue.dequeue(), end='')
        
        print()
        print(queue)

if __name__ == '__main__':
    unittest.main()