from c_stack import Stack
from d_queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
    def __str__(self):
        return str(self.data)
    
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


    def pre_order_stack(self):
        stack = Stack()
        res = Queue()
        link = self.root
        
        while True:
            print(link,stack,res)
            
            if link is not None :
               stack.push(link)
               res.enqueue(link.data)
               if len(res) == self.length: break
            
               if link.left_child is not None:
                   link = link.left_child
                   continue
               
               stack.pop()
               parent = stack.pop()
                     
               if link.right_child is not None:
                   link = link.right_child
                   continue
               
               link = parent.right_child
                   
            continue
               
        return res
    
    def in_order(self, link):
        res = []
        if link.left_child is not None:
            res += self.in_order(link.left_child)
        
        if link is not None :
            res += [link.data]
            
        if link.right_child is not None:
            res += self.in_order(link.right_child)
        
        return res
    
    def in_order_stack(self):
        stack = Stack()
        res = Queue()
        link = self.root
        
        while True:
            
            if link is not None:
                print(link, stack, res)
                stack.push(link)
                
                if link.left_child is not None:
                    link = link.left_child
                    continue
                
                stack.pop()
                res.enqueue(link.data)
                if len(res) == self.length : break
                
                if link.right_child is not None:
                    link = link.right_child
                    continue
                
            parent = stack.pop()
            res.enqueue(parent.data)            
            if len(res) == self.length : break   
            link = parent.right_child
        
        return res
    
    def in_order_stack2(self):
        stack = Stack()
        res = Queue()
        link = self.root
        
        while True:
            if link is not None:
                stack.push(link)
                link = link.left_child
                continue
            
            if not stack.is_empty():
                link = stack.pop()
                res.enqueue(link)
                link = link.right_child
                continue
            
            return res
    
    def post_order(self, link):
        res = []
        
        if link.left_child is not None:
            res += self.post_order(link.left_child)
            
        if link.right_child is not None:
            res += self.post_order(link.right_child)
            
        if link is not None :
            res += [link.data]
        
        return res

    def post_order_stack(self):
        stack = Stack()
        res = Queue()
        link = self.root
        before = None
        
        while True:
            if link is not None:
                stack.push(link)
                
                if self.go_left(link, before):
                    link = link.left_child
                    continue
                
                if self.go_right(link, before):
                    link = link.right_child
                    continue
                
                res.enqueue(link.data)
                if len(res) == self.length : break
                
                before = link
                stack.pop()
                link = stack.pop()
        
        return res
                
            
    def go_left(self, link, before):
        return link.left_child is not None and \
                link.left_child != before and \
                link.right_child != before 
                
    def go_right(self, link, before):
        return link.right_child is not None and \
            link.right_child != before

    # BFS
    def bfs(self):
        queue = Queue()
        queue.enqueue(self.root)
        level = 0

        while not queue.is_empty():
            print(f'level {level} : ', end=' ')

            for i in range(len(queue)):
                node = queue.dequeue()
                print(node.data, end=' ')

                if node.left_child is not None:
                    queue.enqueue(node.left_child)

                if node.right_child is not None:
                    queue.enqueue(node.right_child)
            
            print()
            level += 1