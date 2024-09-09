def move(start_y, start_x, y, x, cnt, vector):
    if cnt != 0 and y == start_y and x == start_x:
        # 최대값인지 검사
        return

    nx = x + dx[vector]
    ny = y + dy[vector]

    if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0:
        visited[ny][nx] = 1
        move(start_y, start_x, ny, nx, cnt+1, vector)
        visited[ny][nx] = 0
    else:   # 범위를 벗어났다면 꺾엇!
        pass



dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    world = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = -1
    visited = [0]*N

    for i in range(N):
        for j in range(N):
            move(i, j, i, j, 0, 0)

    print(max_cnt)