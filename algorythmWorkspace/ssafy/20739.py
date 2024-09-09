# 20739. 고대 유적 2
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0         # 가장 긴 구조물의 길이

    # 가로 탐색
    for i in range(N):
        cnt = 0         # 구조물 길이 초기화
        for j in range(M):
            if arr[i][j] == 1:     # 1을 만났다면
                cnt += 1
            else:                  # 0을 만났다면
                if 2 <= cnt and max_cnt < cnt:
                    max_cnt = cnt   # 그동안의 cnt가 최대값
                cnt = 0
        if 2 <= cnt and max_cnt < cnt:  # 가로열이 끝나도 한번 더 검사
            max_cnt = cnt

    # 세로 탐색
    for i in range(M):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            else:
                if 2 <= cnt and max_cnt < cnt:
                    max_cnt = cnt
                cnt = 0
        if 2 <= cnt and max_cnt < cnt:  # 세로열이 끝나도 한번 더 검사
            max_cnt = cnt
    print(f'#{test_case} {max_cnt}')