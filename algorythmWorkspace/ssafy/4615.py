# 재미있는 오셀로 게임
'''
오셀로라는 게임은 흑돌과 백돌을 가진 사람이 번갈아가며 보드에 돌을 놓아서 최종적으로
보으뎅 자신의 돌이 많은 사람이 이기는 게임이다.

보드는 4x4, 6x6, 8x8(가로, 세로 길이) 크기를 사용한다. 6x6 보드에서 게임을 할 때,
처음에 플레이어는 다음과 같이 돌을 놓고 시작한다. (B : 흑돌, W : 백돌)

4x4, 8x8 보드에서도 동일하게 정가운데 아래와 같이 배치하고 시작한다.
그리고 흑, 백이 번갈아가며 돌을 놓는다.
처음엔 흑부터 시작하는데 이때 흑이 돌을 놓을 수 있는 곳은 다음과 같이 4군데이다.

플레이어는 빈 공간에 돌을 놓을 수 있다.
단, 자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을 경우에만 그 곳에 돌을 놓을 수 있고,
그 때의 상대편의 돌은 자신의 돌로 만들 수 있다.
(여기에서 '사이'란 가로/세로/대각선을 의미한다.)
(2, 3) 위치에 흑돌을 놓은 후의 보드는 다음과 같다.
'''
def f(i, j, bw, N):
    board[i][j] = bw    # 지정된 돌 놓기
    for di, dj in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
        ni, nj = i+di, j+dj
        tmp = []        # 뒤집을 돌의 인덱스를 저장
        while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == op[bw]:  # 반대색 돌이면
            tmp.append((ni, nj))    # 뒤집을 돌을 저장하고
            ni, nj = ni + di, nj + dj # 현재 방향으로 계속 이동
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == bw:
            for p, q in tmp:
                board[p][q] = op[bw]

# 1이면 흑돌, 2이면 백돌
B = 1
W = 2
op = [0, 2, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 보드의 한 변의 길이 N, 돌을 놓는 횟수 M
    play = [list(map(int, input().split())) for _ in range(M)]

    board = [[0]*N for _ in range(N)]   # NxN board 준비, 0 -> N-1 인덱스 사용
    # 중심부 돌을 배치
    # WB
    # BW
    board[N//2-1][N//2-1] = W
    board[N//2-1][N//2] = B
    board[N//2][N//2-1] = W
    board[N//2][N//2] = W

    # 돌 놓기
    for col, row, bw in play:   # 입력 순서 주의, col , row는 1부터 시작
        f(row-1, col-1, bw, N)      # 돌놓기, 뒤집기

    bcnt = wcnt = 0             # 검은돌 개수, 흰돌 개수
    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                bcnt += 1
            elif board[i][j] == W:
                wcnt += 1
    print(f'#{tc} {bcnt} {wcnt}')