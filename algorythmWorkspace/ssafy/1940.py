# 가랏! RC카!
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    command = [list(map(int, input().split())) for _ in range(N)]
    speed = 0   # 현재 속도
    result = 0  # 현재 위치

    for i in range(N):
        if command[i][0] == 1:  # 1이라면 가속
            speed += command[i][1]
        elif command[i][0] == 2:    # 2라면 감속
            speed -= command[i][1]
            if speed < 0:   # 만약 속도 0보다 작다면 0으로 변환
                speed = 0
        result += speed     # 현재 속도만큼 현재 위치 전진
    print(f'#{test_case} {result}')