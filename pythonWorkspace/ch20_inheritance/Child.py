# 자식 클래스
from Parent import *

class Child(Parent): # Parent 클래스로부터 상속 받음
    def __init__(self):
        super().__init__() # 부모 생성자 호출
        self.__c = 20
    
    def show_child(self):
        self.show_parent() # 부모 메소드 사용 가능
        print('자식 클래스의 c : ', self.__c)