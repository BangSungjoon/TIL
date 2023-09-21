score = []
sum = count = 0

for i in range(1, 6):
    a = int(input(f'학생{i} 점수 입력 : '))
    score.append(a)
    sum += a
    if a >= 80:
        count += 1

avg = sum / 5
print('총점 : ',sum)
print('평균 : %.2f'%avg)
print('80점 이상 학생 : %d명'%count)