# 2105. [모의 SW 역량테스트] 디저트 카페
def move(y, x, cnt1, cnt2, cnt3, cnt4):
    global max_cnt
    if cnt1 != 0 and cnt2 != 0 and cnt3 != 0 and cnt4 != 0 and cnt1 == cnt2 and cnt3 == cnt4:
        if max_cnt < cnt1+cnt2+cnt3+cnt4:
            max_cnt = cnt4+cnt3+cnt2+cnt1
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            if k == 0:
                move(ny, nx, cnt1+1, cnt2, cnt3, cnt4)
            elif k == 1:
                move(ny, nx, cnt1, cnt2+1, cnt3, cnt4)
            elif k == 2:
                move(ny, nx, cnt1, cnt2, cnt3+1, cnt4)
            else:
                move(ny, nx, cnt1, cnt2, cnt3, cnt4+1)
            visited[ny][nx] = 0


dy = [-1, 1, -1, 1]
dx = [-1, 1, 1, -1]

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    world = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = -1
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            move(i, j, 0, 0, 0, 0)

    print(max_cnt)