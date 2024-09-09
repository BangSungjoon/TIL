# 16784. 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수
T = int(input())

for test_case in range(1, T+1):
    N, string = input().split()
    N = int(N)
    result = ''

    for s in string:
        if s in 'ABCDEF':
            if s == 'A':
                num = 10
            elif s == 'B':
                num = 11
            elif s == 'C':
                num = 12
            elif s == 'D':
                num = 13
            elif s == 'E':
                num = 14
            else:
                num = 15
        else:
            num = int(s)
        arr = [0,0,0,0]
        for i in range(4):
            if num % 2 == 1:
                arr[3-i] = 1
            num //= 2
        for a in arr:
            result += str(a)

    print(f'#{test_case} {result}')


