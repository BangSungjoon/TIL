from typing import Generic, TypeVar

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # 다음 노드의 주소를 저장
        
    def __str__(self):
        return str(self.data)
      
        
# 덕타이핑 : 객체의 속성 및 메서드의 집합이 객체의 타입을 결정하는 것
# 만약 어떤 새가 오리처럼 걷고, 헤엄치고, 소리를 낸다면 그 새를 오리라고 할 수 있다.
# __init__, __str__, __len__

class LinkedList():
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None  
        
    def __len__(self):
        return self.length
    
    def __str__(self):
        node = self.head
        if node is None : return "[]"
        
        res = "[ "
        
        while node.next:
            res += str(node) + ', '
            node = node.next
        
        res += str(node) + " ]"
        return res     
            
            
    # 매개변수로 전달받은 데이터를 리스트의 마지막에 추가
    def append(self, data):
        node = Node(data)
        
        # 리스트가 비었다면 head에 노드를 넣어줌
        if self.head is None:
            self.head = node
            self.tail = node
        # 마지막 노드를 탐색해서 해당 노드의 next에 새롭게 생성된 노드를 참조
        else:
            self.tail.next = node             
            self.tail = node
            
        self.length += 1
        
    # 매개변수로 전달받은 데이터를 리스트 가장 앞에 추가
    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1

    # 가장 뒤에 있는 데이터를 반환하고 삭제
    def pop(self):
        if self.tail is None: return None
        
        node = self.head
        
        if node.next is None:
            self.head = None
            self.length -= 1
            return node.data
        
        while node.next:            
            prev = node
            node = node.next
            
        res = node.data    
        self.tail = prev
        prev.next = None    
        self.length -= 1
        
        return res
    
    def get(self, idx):   
   
        if idx < 0 or idx >= self.length: 
            raise IndexError("인덱스가 범위를 벗어남")
        
        if(idx == 0) : return self.head.data
        if(idx == self.length - 1): return self.tail.data
        
        node = self.head
        for _ in range(0, idx):
            node = node.next
            
        return node.data
    
    def __setitem__(self, idx, data):        
        if idx < 0 or idx >= self.length: 
            raise IndexError("인덱스가 범위를 벗어남")
        
        if idx == 0 :
            self.head.data = data
            return
        
        if idx == self.length -1:
            self.tail.data = data
            return

        node = self.head
        for _ in range(0, idx):
            node = node.next
        
        node.data = data
            
    def __delitem__(self, idx):
        if idx < 0 or idx >= self.length: 
            raise IndexError("인덱스가 범위를 벗어남")
        
        if idx == 0 :
            self.head = self.head.next
            self.length -= 1
            return
        
        if idx == self.length -1 :
            self.pop()
            return
        
        prev = self.head
        for _ in range(0, idx-1):
            prev = prev.next
            
        prev.next = prev.next.next
        self.length -= 1
        
    def insert(self, idx, data):
        if idx < 0 or idx >= self.length: 
            raise IndexError("인덱스가 범위를 벗어남")
        
        if idx == 0 :
            self.prepend(data)
            return

        if idx == self.length - 1:
            self.append(data)
            return
        
        node = Node(data)
        prev = self.head
        
        for i in range(0, idx-1):
            prev = prev.next
        
        node.next = prev.next
        prev.next = node
        self.length += 1
        
    def __iter__(self):
        return LinkedList.Iterator(self.head) # iterable 객체
    
    class Iterator:
        def __init__(self, node):
            print("생성자 호출")
            self.node = node
            self.call_cnt = 1
        
        def __iter__(self):
            return self
        
        def __next__(self):
            print(f'{self.call_cnt}번째 호출입니다. {self.node}')
            
            if self.node is None:
                 raise StopIteration
            
            self.call_cnt += 1
            
            data = self.node.data
            self.node = self.node.next
            return data            