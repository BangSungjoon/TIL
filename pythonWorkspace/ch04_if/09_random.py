from random import * #모든 함수 import

# 1~10까지의 임의의 정수 (1, 10 포함)
num = randint(1, 10)
print(num)

# 0 < num < 1 사이의 임의의 실수
num = random()
print(num)

# 0 ~ 9까지의 임의의 정수
num = randrange(10) # 10은 포함되지 않음
print(num)

num = randrange(1, 11, 2) # 1~10중에서 홀수
print(num)