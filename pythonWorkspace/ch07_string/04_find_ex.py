# find 메소드 연습문제

cities = '인천 대전 광주 울산 대구 부산'
answer = input('우리 나라 광역시 중 하나 입력 : ')
if (cities.find(answer) > 0) :
    print('정답입니다')
else:
    print('틀렸습니다')

# 또 다른 풀이
if answer in cities:
    print('있음')
else:
    print('없음')