# 무한 반복

while True: # 조건이 무조건 참 : 무한 반복
    print('반복 수행되는 문장')
    answer = input('종료하려면 x 입력 : ')
    if answer == 'x': # 반복문 종료될 조건
        break         # 조건이 참이면 반복문 종료

print('종료했습니다.')