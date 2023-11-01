class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
        
    def __len__(self):
        return self.length
    
    def enqueue(self, data):
        node = Node(data)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        
        self.length += 1
        
    def dequeue(self):
        node = self.front
        if node is None: return None
        
        if node == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        
        self.length -= 1
        return node.data

    def is_empty(self):
        return self.front is None
    
    def __str__(self):
        if self.front is None : return "[]"        
        
        link = self.front
        res = "[ " + str(link.data)
        link = link.next
        
        while(True):
            if(link is None) : break
            res += "," + str(link.data)
            link = link.next
        
        res += " ]" 
        return res