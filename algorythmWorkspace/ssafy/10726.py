# 10726. 이진수 표현
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    for i in range(1, N+1):
        if M % (2 ** i) == 0:
            print(f'#{test_case} OFF')
            break
        M //= 2
    else:
        print(f'#{test_case} ON')