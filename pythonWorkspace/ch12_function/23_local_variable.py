# 지역 변수
def show():
    a = 1       # 함수 내에서 정의된 지역 변수
    a = a + 1   # 값 변경 가능
    print(a)    # 함수 내에서만 사용 가능

show()
# show(a) # 함수 외부에서 사용 불가
# 'a' is not defined