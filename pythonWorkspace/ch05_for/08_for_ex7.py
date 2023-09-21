a = input('이름 입력 : ')
found = False  # 명단에 있는지 여부를 나타내는 상태 변수

for i in ['홍길동', '이몽룡', '성춘향', '변학도']:
    if i == a:
        found = True
        break  # 찾았으면 루프 종료

if found:
    print('명단에 있습니다.')
else:
    print('명단에 없습니다.')