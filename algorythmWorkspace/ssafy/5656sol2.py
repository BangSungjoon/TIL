def boom(x, y, target_arr, visited):
    power = target_arr[y][x]  # 벽돌의 파괴 범위
    target_arr[y][x] = 0  # 현재 벽돌 제거
    visited[y][x] = 1
    for vector in range(4):
        for dis in range(1, power):
            nx = x + dx[vector] * dis
            ny = y + dy[vector] * dis
            if 0 <= ny < H and 0 <= nx < W and target_arr[ny][nx] > 0 and visited[ny][nx] == 0:
                boom(nx, ny, target_arr, visited)

def shoot(level, now_arr):
    global min_block
    # 남은 벽돌 수 세기
    cnt = 0
    for i in range(H):
        for j in range(W):
            if now_arr[i][j]:
                cnt += 1
    # 기저 조건
    # 남은 벽돌이 없으면 종료
    if cnt == 0:
        min_block = 0
        return
    # 구슬을 모두 발사
    if level == N:
        if min_block > cnt:
            min_block = cnt
        return

    # 행을 탐색
    for col in range(W):
        copy_arr = [x[:] for x in now_arr]

        # 가장 맨 위의 블럭 확인
        row = -1
        for h in range(H):
            if copy_arr[h][col]:
                row = h
                break
        if row == -1:
            continue    # 블럭이 없는 열이었다면 패스

        # 블럭의 숫자만큼 상하좌우 파괴
        visited = [[0]*W for _ in range(H)]
        boom(col, row, copy_arr, visited)
        # 자 이제 내려옵시다.
        for c in range(W):  # 전체 열들을 확인
            idx = H - 1  # 벽돌이 위치할 index
            for r in range(H - 1, -1, -1):
                if copy_arr[r][c]:  # 벽돌이 있으면 무조건 swap 하도록
                    # idx 와 r 이 같아도 바꾼다 == 의미없는 교환
                    # 가독성을 위해서 아래와 같이 구현
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1

        shoot(level+1, copy_arr)


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())

for test_case in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    block = 0
    min_block = W*H
    now_remains = 0

    shoot(0, arr)

    print(f'#{test_case} {min_block}')
