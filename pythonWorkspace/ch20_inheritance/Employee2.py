class Employee2:
    def __init__(self, emp_no, emp_name, emp_dpt):
        self.__emp_no = emp_no
        self.__emp_name = emp_name
        self.__emp_dpt = emp_dpt

    def show_emp_info(self):
        print('사번 : ', self.__emp_no)
        print('성명 : ', self.__emp_name)
        print('부서 : ', self.__emp_dpt)