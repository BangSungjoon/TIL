# 1225. [S/W 문제해결 기본] 7일차 - 암호생성기
for _ in range(10):
    test_case = int(input())
    numbers = list(map(int, input().split()))

    # queue 작업을 실행할 빈 리스트 만들기 (8+5 길이)
    password = [0]*13
    for i in range(8):
        password[i] = numbers[i]

    # 사이클 돌기
    cycle = True
    while cycle:    # cycle이 True인 동안 반복
        front = 0   # queue의 처음 (방출할 부분 idx)
        rear = 7    # queue의 꼬리 (입력이 들어올 부분 idx)
        for i in range(1, 6):   # 5번 반복하며 뒤로 이동하는 반복문
            rear += 1   # queue의 입력 idx 증가
            if password[front] - i <= 0:    # 만약 감소한 값이 0이하라면
                password[rear] = 0          # queue에 0 입력
                front += 1
                cycle = False               # while문은 이게 마지막 순회
                break                       # for i in range(1, 6) 정지
            else:                           # 감소한 값이 0 초과라면
                password[rear] = password[front] - i    # 감소된 만큼 queue에 입력
                front += 1                              # 나갔으니 다음 순서 불러오기
        result = password[front:rear+1]     # 결과는 맨 앞부터 꼬리까지
        password[0:8] = result[:]           # 전체 인덱스의 idx 0부터 7까지는 result로 바꿔줌
                                            # 땡겨오기
    print(f'#{test_case}', *result)