class Employee:
    def __init__(self):
        self.__emp_no = 1234
        self.__emp_name = '홍길동'
        self.__emp_dpt = '마케팅'

    def show_emp_info(self):
        print('사번 : ', self.__emp_no)
        print('성명 : ', self.__emp_name)
        print('부서 : ', self.__emp_dpt)