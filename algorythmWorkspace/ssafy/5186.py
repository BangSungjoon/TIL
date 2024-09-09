# 16785. 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2
T = int(input())

for test_case in range(1, T+1):
    N = float(input())
    result = ''

    for i in range(13):
        change = 1
        for _ in range(i+1):
            change *= 0.5
        if N >= change:
            N -= change
            result += '1'
            if N == 0:
                break
        else:
            result += '0'
    else:
        result = 'overflow'

    print(f'#{test_case} {result}')