# 1249. [S/W 문제해결 응용] 4일차 - 보급로
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global min_cnt, n
    q = deque([(0, 0, 0)])

    # 탐색
    while q:
        x, y, cnt = q.popleft()
        if cnt >= min_cnt:  # 가지치기
            continue

        if x == n-1 and y == n-1:   # 목적지에 도착했다면
            min_cnt = cnt
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append((nx, ny, cnt+int(arr[ny][nx])))

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [input() for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    min_cnt = float('inf')
    visited[0][0] = 1
    bfs()

    print(f'#{test_case} {min_cnt}')
