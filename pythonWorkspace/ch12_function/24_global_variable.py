# 전역 변수
a = 1 # 함수 밖에서 정의된 전역 변수

def show():
    print(a)   # 전역변수는 모든 곳에서 사용 가능
    b = 20
    c = b + a  # 전역 변수 사용
    print(c)

def add():
    print(x) # 함수 호출 후에 x가 정의 된다면, 오류 : name 'x' is not defined
    print(a) # 전역변수는 모든 곳에서 사용 가능

x = 100      # 전역 변수는 함수 호출 전에 정의되어야 한다.
show()
add()
print(a)