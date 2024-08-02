T = int(input().strip())

for test_case in range(1, T + 1):
    cards = list(map(int, input().strip()))
    card_count = [0]*12

    for card in cards:
        card_count[card] += 1

    baby_gin = 0
    for i in range(10):
        while card_count[i] >= 3:
            card_count[i] -= 3
            baby_gin += 1
        while card_count[i] >= 1 and card_count[i+1] >= 1 and card_count[i+2] >= 1:
            card_count[i] -= 1
            card_count[i+1] -= 1
            card_count[i+2] -= 1
            baby_gin += 1
    if baby_gin == 2:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')