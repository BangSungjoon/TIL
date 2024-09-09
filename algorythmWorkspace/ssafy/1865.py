# 1865. 동철이의 일 분배
'''
1
3
13 0 50
12 70 90
25 60 100
'''
def work(row, per):
    global result
    if per <= result:
        return
    if row == N:
        # per = per*100
        if result < per:
            result = per
        return

    for k in range(N):
        if visited[k] == 0:
            visited[k] = 1
            work(row+1, per*arr[row][k])
            visited[k] = 0

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j]/100
    visited = [0]*N
    result = 0
    work(0, 1)
    result *= 100

    print(f'#{test_case}', '{:.6f}'.format(result))