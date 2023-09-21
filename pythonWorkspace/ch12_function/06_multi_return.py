# 여러 개의 값 반환
def multi_return() :
    return 1,2,3

# 반환되는 여러 값을 각 변수에 저장
a, b, c = multi_return()
print(a, b, c)

# 반환되는 여러 값을 하나의 변수에 저장
# 튜플로 만들어짐
result = multi_return()
print(result)    # (1, 2, 3)