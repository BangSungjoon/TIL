# 전역변수 연습 문제
def sub(x, y):
    global a

    a = 7 # 전역변수
    x, y = y, x         # 3, 4 -> 4, 3
    b = 3 # 지역변수
    print(a, b, x, y)   # 7 3 4 3

a, b, x, y = 1, 2, 3, 4
sub(x, y)               # 3, 4
print(a, b, x, y)       # 7 2 3 4