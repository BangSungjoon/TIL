class Worker:
    def __init__(self, emp_no, emp_name):
        self.__emp_no = emp_no
        self.__emp_name = emp_name

    def show_work_info(self):
        print('사번 : ', self.__emp_no)
        print('성명 : ', self.__emp_name)