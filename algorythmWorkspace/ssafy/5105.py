# 16649. 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리
T = int(input())

for test_case in range(1, T+1):
    N = int(input())    # 미로의 크기 입력 받기
    maze = [list(map(int, input())) for _ in range(N)]
    result = 0
    # 미로 탐색을 도울 델타
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 방문한 지점 저장하기
    visited = [[0]*N for _ in range(N)]

    # 시작좌표 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x, y = i, j
                break
    visited[x][y] = 1   # 시작점 방문 표시

    # bfs를 이용하여 출구 찾기
    q = []
    q.append([x, y])
    while q:
        tx, ty = q.pop(0)   # 현재 좌표
        for i in range(4):  # 인접한 칸 조사
            next_x = tx + dx[i]
            next_y = ty + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N and maze[next_x][next_y] != 1 and visited[next_x][next_y] == 0:
                visited[next_x][next_y] = visited[tx][ty] + 1
                q.append([next_x, next_y])
                if maze[next_x][next_y] == 3:   # 만약 다음 칸이 도착점이면
                    result = visited[tx][ty] - 1
                    q = []
                    break

    print(f'#{test_case}', result)