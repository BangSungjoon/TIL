# 숫자 카드 21460 16180 4834
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input()))
    count_ai = [0]*10   # 각 숫자별 몇번 나왔는지 기록하는 리스트
    for i in range(N):
        count_ai[ai[i]] += 1
    max_count_ai = 0    # 가장 많은 카드의 숫자
    max_count = 0       # 가장 많은 카드가 몇장인지

    for k in range(10): # 0부터 9까지 순회
        if count_ai[k] >= max_count:
            max_count = count_ai[k]
            max_count_ai = k

    print(f'#{test_case} {max_count_ai} {max_count}')