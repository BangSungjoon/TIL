# 18411. 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합
def arr_sum(cnt, n, current_sum):
    # cnt는 현재 더한 횟수 -> 몇번째 행인가
    # n은 입력 받은 배열의 크기
    # current_sum는 현재까지 더해진 값
    global min_sum
    if current_sum < min_sum:   # 지금까지 더해진 값들이 최솟값보다 작을 때만 동작 (백트래킹), 이미 최솟값을 넘겼으면 가망이 없다~ 계산 안해!
        if cnt == n:     # 만약 더한 횟수가 배열의 길이를 달성했다면 (n번 만큼 더했다)
            min_sum = current_sum       # 전달받은 매개변수(current_sum)이 최솟값이 된다.
        else:            # 아직 더한 횟수가 부족하다면
            for i in range(n):
                if visited[i] == 0:     # 방문한 적이 없다면
                    visited[i] = 1      # 방문 처리
                    arr_sum(cnt+1, n, current_sum+arr[cnt][i])      # 현재 행렬의 값 만큼 합산 한 뒤 전달
                    visited[i] = 0      # 방문 하지 않음으로 바꾼다.

T = int(input())

for test_case in range(1, T+1):
    N = int(input())    # 배열의 사이즈 NxN 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N     # 방문 기록 배열
    min_sum = 91        # 배열의 최솟값 (91을 넘길 수 없다.)
    arr_sum(0, N, 0)    # 더한 횟수는 0에서 시작, 배열의 크기 N, 현재까지 더해진 값 0

    print(f'#{test_case} {min_sum}')