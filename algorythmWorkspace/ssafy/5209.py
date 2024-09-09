# 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
def dfs(row, price):
    global N, min_price
    if price < min_price:
        if row == N:
            min_price = price
            return

        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                dfs(row+1, price+arr[row][i])
                visited[i] = 0

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    min_price = float('inf')

    dfs(0, 0)

    print(f'#{test_case} {min_price}')