# 구구단의 단수를 입력 받아서 해당 구구단 출력하는 프로그램

a = int(input('단 수 입력 : '))

for i in range(1, 10):
    print(f'{a} * {i} = {a*i}')