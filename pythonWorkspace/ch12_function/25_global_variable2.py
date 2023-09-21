# 전역 변수 변경 : global 지정
a = 1 # 함수 밖에 정의된 전역변수

def add():
    a = 100  # 함수 내에서 정의된 지역 변수
    print(a) # 전역변수 사용 가능

def add2():
    global a     # 전역변수임을 지정
    a = a + 100  # 전역변수 값 변경
    print(a)     # 전역변수 사용 가능

add()
add2()