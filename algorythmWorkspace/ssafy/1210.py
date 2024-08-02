import sys
sys.stdin = open('input.txt', 'r')


for test_case in range(1, 11):
    tc = int(input())
    leader = [list(map(int, input().split())) for _ in range(100)]
    y = 99
    dx = [0, -1, 1]
    dy = [-1, 0, 0]
    k = 0

    for x in range(100):
        if leader[y][x] == 2:
            break

    while y != 0:
        if k == 0:  # 위로 상승하는 중이라면
            if x-1 > 0 and leader[y][x-1] == 1:     # 꺾인 방향으로 방향 전환
                k = 1
            if x+1 < 100 and leader[y][x+1] == 1:
                k = 2
        else:       # 가로로 이동중일 때
            if not (0 <= x+dx[k] <= 99):
                k = 0
            if not leader[y+dy[k]][x+dx[k]] == 1:
                k = 0
        x += dx[k]
        y += dy[k]

    print(f'#{test_case} {x}')