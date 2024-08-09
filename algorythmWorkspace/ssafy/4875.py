T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0

    # 2의 위치를 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                stack = [[i, j]]
                visited[i][j] = 1

    # 스택이 존재하는 동안 반복
    while stack:
        x, y = stack.pop()
        visited[x][y] = 1
        # 갈 수 있는 모든 방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] != 1 and maze[nx][ny] != 1:
                if maze[nx][ny] == 3:
                    result = 1
                    break
                stack.append([nx, ny])

    print(f'#{test_case} {result}')