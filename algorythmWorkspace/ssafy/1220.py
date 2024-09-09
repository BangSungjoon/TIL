# 1220. [S/W 문제해결 기본] 5일차 - Magnetic
for test_case in range(1, 11):
    size = int(input())
    table = [list(map(int, input().split())) for _ in range(size)]
    cnt = 0                         # 교착 상태의 개수
    deadlock = False                # 교착 상태

    for i in range(size):
        for j in range(size):       # 열 탐색
            if table[j][i] == 1:    # 1을 만났다면
                deadlock = True     # 교착상태 대기
            elif table[j][i] == 2:  # 2를 만났다면
                if deadlock:        # 대기중인 교착 상태가 있다면
                    cnt += 1        # 교착 상태의 개수 + 1
                deadlock = False    # 교착 상태 대기 풀기
        deadlock = False            # 매 열 순회가 끝날 때마다 초기화

    print(f'#{test_case} {cnt}')