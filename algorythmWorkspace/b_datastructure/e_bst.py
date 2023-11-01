from c_stack import Stack
from d_queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
    def __str__(self):
        return self.data
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.length = 0 
    
    def __len__(self):
        return self.length
        
    def insert(self, data):
        node = Node(data)
        
        if self.root is None:
            self.root = node
            self.length += 1
            return
        
        link = self.root
        while True:
            if data <= link.data:
                if link.left_child is None:
                    link.left_child = node
                    break
               
                link = link.left_child
            else:
                if link.right_child is None:
                    link.right_child = node
                    break
                link = link.right_child
                
        self.length += 1
        
    def find(self, data):
        link = self.root
        while True:
            if link is None : return False
            if data == link.data : return True
            if data < link.data:
                link = link.left_child
            else:
                link = link.right_child
    
    def pre_order(self, link):
        res = []
        if link is not None :
            res += [link.data]
        
        if link.left_child is not None:
            res += self.pre_order(link.left_child)
            
        if link.right_child is not None:
            res += self.pre_order(link.right_child)
        
        return res
    
    
    
