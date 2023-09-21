# 자식 클래스
from Employee2 import *

class Manager2(Employee2): 
    def __init__(self, emp_no, emp_name, emp_dpt, position):
        super().__init__(emp_no, emp_name, emp_dpt)
        # 부모 클래스 생성자 호출하면서 매개변수 전달
        self.__position = position
    
    def show_manager_info(self):
        self.show_emp_info()
        print('직위 : ', self.__position)