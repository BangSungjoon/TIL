# 무한 반복 연습문제
# 노래방 
i = 1
money = 10000
while True: # 조건이 무조건 참 : 무한 반복
    print(f'노래를 {i}곡 불렀습니다.')
    money -= 2000
    if money == 0: # 반복문 종료될 조건
        break         # 조건이 참이면 반복문 종료
    else:
        print(f'현재 {money}원 남았습니다.')
    i += 1

print('잔액이 없습니다. 종료합니다.')