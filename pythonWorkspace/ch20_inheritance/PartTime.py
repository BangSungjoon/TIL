# 자식 클래스
from Worker import *

class PartTime(Worker): 
    def __init__(self, emp_no, emp_name, money, work_time):
        super().__init__(emp_no, emp_name)
        self.__money = money
        self.__work_time = work_time
    
    def calculate_salary(self):
        self.__total = self.__money * self.__work_time

    def show_pt_info(self):
        self.show_work_info()
        print('시급 : ', self.__money,'원')
        print('근무시간 : ', self.__work_time,'시간')
        print('급여 : ', self.__total,'원')