T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = [[0 for j in range(10)] for i in range(10)]
    N = int(input())

    for _ in range(N):
        color_area = list(map(int, input().split()))
        if color_area[-1] == 1:
            for i in range(color_area[0], color_area[2]+1):
                for j in range(color_area[1], color_area[3]+1):
                    arr[i][j] += 1
        if color_area[-1] == 2:
            for i in range(color_area[0], color_area[2]+1):
                for j in range(color_area[1], color_area[3]+1):
                    arr[i][j] += 100

    count = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] >= 101:
                count += 1
    print(f'#{test_case} {count}')