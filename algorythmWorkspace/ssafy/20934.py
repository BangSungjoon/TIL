# 방울 마술
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    s, k = input().split()
    bell = 0    # 방울의 현재 위치

    for i in s: # 방울의 현재 위치 찾기
        if i == 'o':
            break
        bell += 1

    if int(k) == 0: # 만약 k가 0이라면 제자리
        print(f'#{test_case} {bell}')
    else:
        for _ in range(int(k)):
            if bell - 1 >= 0:   # 확률이 같다면 가장 왼쪽이 정답이기 때문에
                bell -= 1       # 왼쪽으로 보낼 수 있다면 왼쪽으로 보낸다.
            else:               # 보낼 수 없다면
                bell += 1       # 오른쪽으로
        print(f'#{test_case} {bell}')
