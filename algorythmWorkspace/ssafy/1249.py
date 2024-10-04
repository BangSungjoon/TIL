# 1249. [S/W 문제해결 응용] 4일차 - 보급로
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, cnt):
    global min_cnt, n
    # 만약 현재 복구 시간이 최소 복구 시간보다 크다면 넌 가망이 없다
    if cnt >= min_cnt:
        return
    # 목적지에 도착했다면 현재 복구 시간이 최소 복구 시간
    if x == n-1 and y == n-1:
        min_cnt = cnt
        return

    # 벡터탐색 들어가요
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] > cnt + arr[ny][nx]:
            visited[ny][nx] = cnt + arr[ny][nx]  # 방문처리
            dfs(nx, ny, cnt + arr[ny][nx])

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int,list(input()))) for _ in range(n)]
    visited = [[999999]*n for _ in range(n)]
    min_cnt = float('inf')
    # visited[0][0] = 1
    dfs(0, 0, 0)

    print(f'#{test_case} {min_cnt}')
