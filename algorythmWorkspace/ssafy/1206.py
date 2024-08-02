T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    N = int(input())
    building = list(map(int, input().split()))

    for i in range(2, N-2):
        nav = [building[i-2], building[i-1], building[i+1], building[i+2]]
        if building[i] > max(nav):
            result += building[i] - max(nav)

    print(f'#{test_case} {result}')