name = "홍길동"
no = 2020001
year = 4
grade = 'A'
average = 93.5

print("성명 : %s" %name)
print("학번 : %d" %no)
print("학년 : %d" %year)
print("학점 : %c" %grade)
print("평균 : %.1f" %average) # %.숫자f = 소수점 표시하고 싶은 자리수

# 퍼센트로 %로 출력
print("10%")

rate = 80
print("출력률 : %d%%" %rate)

# 2개의 변수 출력 시 : 여러 개의 변수를 반드시 괄호로 묶는다
total = 250
average = 83.333333
print("%d, %.2f" % (total, average))