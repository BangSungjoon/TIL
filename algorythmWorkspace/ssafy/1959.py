# 1959. 두 개의 숫자열
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
    maximum = None

    if N < M:
        for i in range(M-N+1):
            current_sum = 0
            for j in range(N):
                current_sum += Ai[j]*Bi[i+j]
            if maximum == None or maximum < current_sum:
                maximum = current_sum
    else:
        for i in range(N-M+1):
            current_sum = 0
            for j in range(M):
                current_sum += Ai[j+i] * Bi[j]
            if maximum == None or maximum < current_sum:
                maximum = current_sum

    print(f'#{test_case} {maximum}')