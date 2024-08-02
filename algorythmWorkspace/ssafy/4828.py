T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))

    max_ai = ai[0]
    min_ai = ai[0]

    for a in ai:
        if a > max_ai:
            max_ai = a
        if a < min_ai:
            min_ai = a

    print(f'#{test_case} {max_ai-min_ai}')