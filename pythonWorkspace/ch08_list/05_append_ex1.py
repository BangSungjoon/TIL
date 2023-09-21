# 3명의 회원을 입력받아 출력하는 연습문제
people = []

for i in range(3):
    people.append(input('회원 입력 : '))

print('회원 명단 : ', end='')
for i in range(len(people)):
    print(f'{people[i]}', end=' ')