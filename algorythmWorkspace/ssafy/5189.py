# 18685. 5189. 전자카트
def cart(row, lev, total):
    global N, min_total
    if total < min_total:
        if lev == N - 1:
            total += area[row][0]
            if total < min_total:
                min_total = total
            return

        for i in range(N):
            if row != i and visited[i] == 0:
                visited[i] = 1
                cart(i, lev + 1, total + area[row][i])
                visited[i] = 0


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    min_total = float('inf')
    visited = [0] * N
    visited[0] = 1

    cart(0, 0, 0)
    print(f'#{test_case} {min_total}')