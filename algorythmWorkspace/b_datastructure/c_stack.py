class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return str(self.data)
    
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)

        if self.top is None: # 맨 위 노드가 비었다면
            self.top = node # 입력된 노드는 맨 위 노드가 된다
        else:
            node.next = self.top
            self.top = node
    
    def pop(self):
        if self.top is None : return None
        res = self.top.data
        self.top = self.top.next
        return res
    
    def peak(self):
        if self.top is None : return None
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def __str__(self):
        if self.top is None : return "[]"
        
        link = self.top
        res = "[ " + str(link.data)
        link = link.next
        while(True):
            if(link is None) : break
            res += "," + str(link.data)
            link = link.next

        res += " ]"
        return res