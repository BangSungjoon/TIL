T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())        # N은 화덕의 크기, M은 피자의 개수
    cheeze = list(map(int, input().split())) # 피자 위의 치즈의 양
    pizza = [0]*M

    # 가장 마지막까지 남아있는 피자 번호를 알아내라
    # 피자에 번호 부여
    for i in range(M):
        pizza[i] = [i+1, cheeze[i]]

    # 먼저 넣은게 먼저 나오니 큐로 접근!
    oven = []
    for _ in range(N):
        oven.append(pizza.pop(0))   # 오븐에 피자 N번만큼 넣어주기
    while oven:                     # 오븐에 피자가 있는 동안 반복
        check = oven.pop(0)         # 오븐 안 1번자리의 피자 꺼내보기
        check[1] //= 2              # 치즈가 녹아부렀으
        if check[1] == 0:           # 다 녹았으면
            if pizza:               # 밖에 아직 불맛을 안본 피자가 있다면
                oven.append(pizza.pop(0))   # 오븐에 넣어버려
        else:                       # 다 안녹았으면
            oven.append(check)      # 다시 오븐행

    print(f'#{test_case} {check[0]}')