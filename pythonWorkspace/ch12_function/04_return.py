# 반환값이 있는 함수
def add():
    num1 = int(input('숫자1 입력 : '))
    num2 = int(input('숫자2 입력 : '))
    return num1 + num2

# 함수 호출하면 결과값이 함수명 우치로 반환
# 반환값을 변수에 저장해서 사용하는 경우
result = add()
print('합 : ', result)

# 반환값을 출력문에서 바로 사용하는 경우
print('합 : ', add())