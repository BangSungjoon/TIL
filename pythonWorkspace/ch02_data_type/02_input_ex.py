korean = eval(input("국어 점수 입력 : "))
en = eval(input("영어 점수 입력 : "))
math = eval(input("수학 점수 입력 : "))
avg = (korean + en + math)/3 # 형변환하지 않아도 소수점이하 값 유지

print("총점 : " + str(korean + en + math))
print("평균 : %.2f" %avg)