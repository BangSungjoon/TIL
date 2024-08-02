# 16285. 4843. 특별한 정렬

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))
    result = [0] * 10

    # ai 정렬하기
    for i in range(N-1, 0, -1):
        for j in range(i):
            if ai[j] > ai[j+1]:
                ai[j], ai[j+1] = ai[j+1], ai[j]

    # 특별한 정렬하기
    cnt = -1
    for i in range(0, 10, 2):
        result[i] = ai[cnt]
        cnt -= 1

    cnt2 = 0
    for i in range(1, 10, 2):
        result[i] = ai[cnt2]
        cnt2 += 1

    print(f'#{test_case}',*result)