# for ~ else
for i in range(5):
    print(i, end=' ')
else:
    print('for문 반복 종료 후 else 수행')

# for ~ else 사용하지 않아도 결과 동일
for i in range(5):
    print(i, end=' ')

print('for문 반복 종료 후 else 수행')

#####################################################
# break가 있을 때 차이
for i in range(5):
    print(i, end=' ')
    if i == 2:
        break # for문 중단
else: # for문 중단되면 이 부분 수행하지 않음
    print('for문 반복 종료 후 else 수행')

for i in range(5):
    print(i, end=' ')
    if i == 2:
        break

print('for문 반복 종료 후 else 수행')

# 사용 예
name_list = ['홍길동','이몽룡','성춘향']
search_name = '박지성'

for name in name_list:
    if name == search_name:
        print('있음')
        break
else:
    print('없음')