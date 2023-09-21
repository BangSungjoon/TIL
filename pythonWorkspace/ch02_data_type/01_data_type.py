name = "홍길동"
age = 20

print(name, age)
print(name + "의 나이 : " + str(age)) # 문자열 연결 연산자 + 사용 시 오류
# str() 형변환

# 숫자 입력 : input() 함수 사용
# num = input("숫자 입력 : ")
# print(num + str(5)) 오류 발생

num = int(input("숫자 입력 : "))
print(num + 5)

num = eval(input('숫자 입력 : ')) # eval() : 정수/실수 다 입력 가능
print(num + 5)

# eval() 함수 : 연산식 입력 가능 / 연산 결과 반환
result = eval(input("수식 입력 : ")) # 10 + 5
print(result)