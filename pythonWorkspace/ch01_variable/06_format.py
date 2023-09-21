# format() 함수 사용

weight = 70
height = 1.72
bmi = 22.8571

# format() 함수 사용 : 여러 변수 값 출력 {}만 지정하는 경우
print("몸무게 : {}, 키 : {}, bmi : {}".format(weight, height, bmi))

# {} 안에 위치 지정하는 경우
print("키 : {1}, 몸무게 : {0}, bmi : {2}".format(weight, height, bmi))

# 소수 자릿수 지정 : {0:.2f} ({위치:.소수점자리수f})
print("키 : {1:.1f}, 몸무게 : {0}, bmi : {2:.2f}".format(weight, height, bmi))

# 천단위 구분 기호
x = 1000
y = 2000
print("x : ", format(x, ','))
print(format(x, ','), format(y, ','))