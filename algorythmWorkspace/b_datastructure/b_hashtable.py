class Node:
    def __init__(self, key:str, data):
        self.key = key
        self.data = data
        self.next = None

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return 31 * sum([ord(s) for s in self.key]) # aaabb [97,97,97,98,98]
    
    def __str__(self):
        return "{key=" + self.key + ", data=" + self.data + "}"


class DuplicateKey(RuntimeError): pass

class HashTable:
    def __init__(self, length = 4):
        self.table_length = length
        self.table = [None for _ in range(self.table_length)]
        self.length = 0
    
    # self.table 의 어떤 인덱스에 저장할지 결정하기 위한 해시함수
    def hash(self, node):
        return hash(node) % self.table_length 
    
    def __add(self, link, node):
        if(link == node) : raise DuplicateKey

    def __set(self, link, node):
        if(link == node) : 
            link.data = node.data
            raise DuplicateKey
    
    
    def __add_context(self, key:str, data, callback_fn):
        if type(key) is not str:
            raise TypeError("key가 str이 아님")
        
        node = Node(key, data)
        index = self.hash(node)

        if self.table[index] is None:
            self.table[index] = node
        else:
            link = self.table[index]          

            while(True):                
                try:
                    callback_fn(link,node)
                except:
                    return
                
                if(link.next is None):
                    link.next = node
                    break
                
                link = link.next                                           

        self.length += 1
    
    # 데이터를 추가, 만약 같은 키가 존재할 경우 데이터를 덮어쓰지 않음
    def add(self, key:str, data):
        # 파이썬의 함수는 1급객체
        # 1급객체 : 값으로 다룰 수 있는 것
        #  return 할 수 있고, 매개변수로 전달할 수 있고, 변수에 담을 수 있음
        self.__add_context(key, data, self.__add)


    # 데이터를 추가 및 수정, 같은 키가 존재하면 데이터를 덮어씀
    def set(self, key:str, data):
       self.__add_context(key, data, self.__set)
        
    
    def __str__(self):
        res = []

        for link in self.table:
            if link is None : continue
            
            while(True):
                res.append(str(link))
                if link.next is None : 
                    break
                link = link.next

        return str(res)
    
    def get(self, key: str):
        if type(key) is not str:
            raise TypeError("key가 str이 아님")
        
        node = Node(key, None)
        index = self.hash(Node(key, None))
        link = self.table[index]

        if link is None : return None
        if link == node : return link.data
        link = link.next

        while(True):
            if link is None : break
            if link == node : return link.data
            link = link.next

        return None
    
    def remove(self, key:str):
        pass # 과제 : 탐색 + 삭제


    def __contains__(self, key:str):
        if type(key) is not str:
            raise TypeError("key가 str이 아님")
        
        return True if self.get(key) is not None else False


    def __iter__(self):
        return HashTable.Iterator(self)

    class Iterator:
        def __init__(self, hashtable):
            self.table = hashtable.table
            self.size = hashtable.length
            self.p1 = 0
            self.node = None
            self.iter_cnt = 0

        def __iter__(self):
            return self
        
        def __next__(self):
            if self.iter_cnt >= self.size:
                raise StopIteration
            
            while self.table[self.p1] is None:
                self.p1 += 1

            if self.node is None:
                self.node = self.table[self.p1]
            
            if self.node.next is None:
                self.p1 += 1

            res = self.node.data

            self.iter_cnt += 1
            self.node = self.node.next
            return res
