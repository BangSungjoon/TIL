# 10580. 전봇대
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    # 전봇대
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort()
    cnt = 0

    for i in range(1, N):
        for j in range(i):
            # a가 더 아래 있지만 b가 더 높으면 교차점
            if arr[j][1] > arr[i][1]:
                cnt += 1

    print(f'#{test_case} {cnt}')