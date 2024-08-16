# 1226. [S/W 문제해결 기본] 7일차 - 미로1
def bfs(x, y, N):
    # 준비
    visited = [[0]*N for _ in range(N)]
    queue = []
    queue.append([x, y])
    visited[x][y] = 1   # 시작점 다녀가요~

    # 탐색
    while queue:
        tx, ty = queue.pop(0)   # 현재 x, y 좌표
        for i in range(4):
            next_x = tx + dx[i]
            next_y = ty + dy[i]
            # 진행할 방향에 도착점이 있다면
            if maze[next_x][next_y] == 3:
                return 1
            # 인접한 칸 중에 길이 있다면
            if 0 <= next_x < N and 0 <= next_y < N and visited[next_x][next_y] != 1 and maze[next_x][next_y] == 0:
                queue.append([next_x, next_y])  # 다음에 갈 경로 추가
                visited[next_x][next_y] = 1     # 방문 표시

    return 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(10):
    test_case = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    # 미로의 시작점과 도착점 찾기
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start_x, start_y = i, j
                break

    result = bfs(start_x, start_y, 16)

    print(f'#{test_case} {result}')