# 18684. 5188. 최소합
def dfs(x, y, total):
    global result, N
    if total < result:
        if x == N-1 and y == N-1:
            result = total
            return

        for i in range(2):
            if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N and visited[y+dy[i]][x+dx[i]] == 0:
                visited[y+dy[i]][x+dx[i]] = 1
                dfs(x+dx[i], y+dy[i], total+arr[y+dy[i]][x+dx[i]])
                visited[y+dy[i]][x+dx[i]] = 0

T = int(input())

for test_case in range(1, T+1):
    N = int(input())    # 가로 세로 칸 수
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, 0]
    dy = [0, 1]
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = 1
    result = float('inf')   # 최소합계 초기값

    dfs(0, 0, arr[0][0])

    print(f'#{test_case} {result}')
