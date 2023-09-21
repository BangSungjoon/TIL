# 예외 발생하는 경우 : except 문 수행
# 예외가 발생하지 않는 경우 : else 문 수행

try:
    num = int(input('정수 입력 : '))
except ValueError:
    print('정수가 아닙니다')
else:
    print(num)

# pass
# 오류 발생 시 아무것도 수행하지 않고 넘어갈 때 사용

try:
    num = int(input('정수 입력 : '))
except ValueError:
    pass # 아무것도 수행하지 않고 다음 문장 수행
else:
    print(num)

# finally : 예외 발생 여부와 상관없이 항상 수행되는 블록
try:
    num = int(input('정수 입력 : '))
except ValueError:
    pass # 아무것도 수행하지 않고 다음 문장 수행
else:
    print(num)
finally:
    print('종료')