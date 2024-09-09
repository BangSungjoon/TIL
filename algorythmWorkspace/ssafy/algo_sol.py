# 월말평가2 - 알고리즘 기본
# 외계인 자리 배정
def zari(num, cnt, row, current_sum):
    # num은 외계인의 수, cnt는 더한 횟수, current_sum은 현재 위험도 합
    global min_sum
    if current_sum < min_sum:
        if cnt == num-1:            # 외계인을 전부 세웠다면
            min_sum = current_sum
        else:                       # 아직 외계인 다 못세웠다면
            for i in range(num):
                if row != i and visited[i] == 0:
                    visited[i] = 1
                    zari(num, cnt+1, i, current_sum+arr[row][i])
                    visited[i] = 0

T = int(input())

for test_case in range(1, T+1):
    N = int(input())        # 외계인의 수
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 999999999

    for k in range(N):
        visited = [0] * N  # 방문 기록
        visited[k] = 1
        zari(N, 0, k, 0)
    print(f'#{test_case} {min_sum}')