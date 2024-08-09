def pascal(idx, n):
    if n >= 1 and arr[idx][n] == 0:
        arr[idx][n] = pascal(idx-1, n-1) + pascal(idx-1, n)
    return arr[idx][n]

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [[0 for j in range(i+1)] for i in range(N)]
    print(f'#{test_case}')
    for i in range(N):
        arr[i][0] = 1
        arr[i][-1] = 1
        for j in range(i+1):
            print(pascal(i, j), end=' ')
        print()
