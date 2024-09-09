# 10726. 이진수 표현
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    number = ''
    for _ in range(N):
        number += '1'

    number = int(number, 2)
    if M & number == number:
        print(f'#{test_case} ON')
    else:
        print(f'#{test_case} OFF')