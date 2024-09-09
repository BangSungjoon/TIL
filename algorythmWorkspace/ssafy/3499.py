# 3499. 퍼펙트 셔플
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(input().split())
    new_deck = [0]*N
    center = N // 2                 # 증앙

    if N % 2 == 1:                  # N이 홀수이면
        for i in range(center):
            new_deck[i*2] = arr[i]
            new_deck[i*2+1] = arr[center + i + 1]
        new_deck[-1] = arr[center]
    else:
        for i in range(center):
            new_deck[i*2] = arr[i]
            new_deck[i*2+1] = arr[center + i]

    print(f'#{test_case}', *new_deck)