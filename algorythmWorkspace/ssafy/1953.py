# 1953. [모의 SW 역량테스트] 탈주범 검거
def runrun(y, x, hour):
    global cnt
    visited[y][x] = 1  # 방문 처리
    cnt += 1
    # 기저 조건: 도망 시간이 다됐다면 그동안 방문한 곳 개수 세기
    if hour <= 0:
        return
    # 해당 블럭 타입별로 나누기
    # 위를 보는 구조물
    if under_map[y][x] in {1, 2, 4, 7}:
        if 0 <= y-1 < N and visited[y-1][x] == 0 and under_map[y-1][x] in {1, 2, 5, 6}:
            runrun(y-1, x, hour-1)
    # 아래를 보는 구조물
    if under_map[y][x] in {1, 2, 5, 6}:
        if 0 <= y+1 < N and visited[y+1][x] == 0 and under_map[y+1][x] in {1, 2, 4, 7}:
            runrun(y+1, x, hour-1)
    # 왼쪽을 보는 구조물
    if under_map[y][x] in {1, 3, 6, 7}:
        if 0 <= x-1 < M and visited[y][x-1] == 0 and under_map[y][x-1] in {1, 3, 4, 5}:
            runrun(y, x-1, hour-1)
    # 오른쪽을 보는 구조물
    if under_map[y][x] in {1, 3, 4, 5}:
        if 0 <= x+1 < M and visited[y][x+1] == 0 and under_map[y][x+1] in {1, 3, 6, 7}:
            runrun(y, x+1, hour-1)

T = int(input())

for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    under_map = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    # 인접리스트를 만들자
    # adj_l = [[], [1, 2, 5, 6], [1, 2, 5, 6], [], [1, 2, 5, 6], ]
    cnt = 0
    runrun(R, C, L-1)

    print(f'#{test_case} {cnt}')
