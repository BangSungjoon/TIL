# 자식 클래스
from Employee import *

class Manager(Employee): 
    def __init__(self):
        super().__init__() # 부모 클래스 생성자 호출
        self.__position = '대리'
    
    def show_manager_info(self):
        self.show_emp_info()
        print('직위 : ', self.__position)