# 각 학생별 점수 리스트 생성
kim = [90, 85, 70]
lee = [88, 79, 92]
park = [100, 100, 100]
kang = [90, 60, 70]

# 전체 학생 리스트 생성
students = [kim, lee, park, kang]
print(students)

# students 크기 확인
print(len(students)) # 4

# 점수 출력
for scores in students:
    print(scores)

# 점수, 총점, 평균 출력
print('---성적표 (점수, 총점, 평균)---')
for scores in students:
    total = sum(scores)
    avg = total / len(students)
