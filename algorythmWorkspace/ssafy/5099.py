# 16632. 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())    # N: 오븐의 크기, M: 피자 개수
    pizza = list(map(int, input().split()))
    for i in range(M):
        pizza[i] = [i, pizza[i]]
    oven = []

    # 처음에 오븐에 피자 가득 채워주기
    for _ in range(N):
        oven.append(pizza.pop(0))

    # 오븐에 피자가 하나 남을 때 까지
    while len(oven) != 1:
        # 맨 앞의 피자 빼주기
        check_pizza = oven.pop(0)
        # 만약 피자의 치즈가 0이라면
        if check_pizza[1] // 2 == 0:
            if pizza:
                oven.append(pizza.pop(0))
        else:   # 피자의 치즈가 0이 아니라면
            oven.append([check_pizza[0], check_pizza[1]//2])
    # while문을 빠져나왔으니 오븐에 피자는 하나만 존재한다.
    result = oven[0][0] + 1     # 오븐에 있는 피자의 인덱스 + 1 = 피자 번호
    print(f'#{test_case} {result}')