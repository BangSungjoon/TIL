# 16632. 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기
T = int(input())
'''
현재 문제 : 피자를 꺼낸다 한들 그 꺼낸 피자의 인덱스를 모르겠다.
'''

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    for i in range(M):
        pizza[i] = [i, pizza[i]]
    # 오븐의 초기값 = N번까지의 피자 + N만큼의 빈 공간
    oven = pizza[:N] + [[0,0]]*N
    # 오븐에 들어간 피자 기록
    visited = [1]*N + [0]*(M-N)
    # 치즈가 다 녹은 피자 개수
    cnt = 0

    # 얼마동안 돌래? 치즈가 다 녹은 피자의 수가 M-1개 될 때까지!
    while cnt < M:
        front = 0
        rear = N-1
        # 한번에 N번 만큼 구우니 N번 반복
        for i in range(N):
            rear += 1
            # 출구쪽 피자 꺼내기, 치즈는 나누기 2가 된다.
            pizza_check = oven[front][1]//2
            # 만약 꺼낸 피자의 치즈가 0이라면
            if pizza_check == 0:
                # 오븐에 안들어간 피자 찾기
                if 0 in visited:    # 오븐에 안들어간 피자가 있다면
                    for i in range(M):
                        if visited[i] == 0:
                            visited[i] = 1  # 오븐에 들어간 걸로 바꾸고
                            oven[rear] = pizza[i]  # 오븐의 출구쪽에 새 피자를 넣어주기
                            cnt += 1
                            break
                else:   # 오븐에 안들어간 피자가 없다면
                    cnt += 1  # 피자 오븐에서 꺼내기
                    oven[rear] = [9999, 9999]
            # 녹은 치즈의 양이 0이 아니라면
            else:
                # 오븐의 출구쪽에 치즈가 절반 준 피자 넣기
                oven[rear] = [oven[front][0], pizza_check]
            front += 1
        # 반복이 끝나고 oven의 앞쪽으로 다시 정렬
        oven = oven[front:rear+1] + [[0,0]]*N

    print(oven)