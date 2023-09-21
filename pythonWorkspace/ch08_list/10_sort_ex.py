score = []
sum = count = 0
student = int(input('학생 수 입력 : '))

for i in range(1, student+1):
    a = int(input(f'학생{i} 점수 입력 : '))
    score.append(a)
    sum += a
    if a >= 80:
        count += 1

avg = sum / student
print('총점 : ',sum)
print('평균 : %.2f'%avg)
print('80점 이상 학생 : %d명'%count)
score.sort(reverse=True)
print('점수 내림차순 정렬 : ', score)