from random import *

you = input("YOU 입력 : ")
com = randint(1, 3)

if you == '가위' :
    you = int(1)
elif you == '바위' :
    you = int(2)
else:
    you = int(3)

result = you - com

# 당신이 이기는 경우
# 1 - 3 = -2
# 2 - 1 = 1
# 3 - 2 = 1

if result == 1 or result == -2 :
    print('당신이 이겼습니다.')
elif result == 0 :
    print('비겼습니다.')
else:
    print('컴퓨터가 이겼습니다.')

if com == 1 :
    com = '가위'
elif com == 2 :
    com = '바위'
else:
    com = '보'
print('컴퓨터는 %s 입니다.' %com)