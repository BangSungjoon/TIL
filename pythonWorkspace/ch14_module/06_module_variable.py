from show_info import *

print(age)

def get_age():
    global age
    age = age + 10 # 전역변수 값 변경 (30)
    print(age) # 전역변수 사용 가능

get_age()

# 변수만 import
from show_info import age

print(age)