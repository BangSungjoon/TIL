T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    result = []

    for i in range(N-M+1):
        n = 0
        for j in range(M):
            n += arr[i+j]
        result.append(n)

    print(f'#{test_case} {max(result)-min(result)}')