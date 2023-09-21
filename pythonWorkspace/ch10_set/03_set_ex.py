# 파티에 참석한 사람이 다음과 같을 때 집합 생성

print('파티에 참석한 모든 사람')
partyA = {'Park', 'Kim', 'Lee'}
partyB = {'Park', '길동', '몽룡'}
print(f'{partyA | partyB}')
print('------------------------------------')
print('2개의 파티에 모두 참석한 사람')
print(f'{partyA & partyB}')
print('------------------------------------')
print('파티A에만 참석한 사람')
print(f'{partyA - partyB}')
print('------------------------------------')
print('파티B에만 참석한 사람')
print(f'{partyB - partyA}')