print('1: 가위, 2: 바위, 3: 보')
hong = int(input("홍길동 입력 : "))
lee = int(input("이몽룡 입력 : "))

result = hong - lee

# hong이 이기는 경우
# 1 - 3 = -2
# 2 - 1 = 1
# 3 - 2 = 1

if result == 1 or result == -2 :
    print('홍길동이 이겼습니다.')
elif result == 0 :
    print('비겼습니다.')
else:
    print('이몽룡이 이겼습니다.')