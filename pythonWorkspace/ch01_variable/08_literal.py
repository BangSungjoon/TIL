# 리터럴 : 변수에 저장되는 값 자체

# 문자열 리터럴
str1 = '홍길동'
str2 = 'python'
str3 = '''python programming'''
str4 = '''파이썬 프로그래밍'''
str5 = '''여러 줄로 
나누어
출력해도 됨'''

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)

# 논리값 리터럴 (Boolean Literals)
t = True
f = False
print(t, f)
print(type(t)) # <class 'bool'>

# 특수 리터럴
name = "홍길동"
phone = '' # 공백
address = None
print(name, phone, address)
print(type(phone)) # '' 공백 : <class 'str'>
print(type(address)) # None : <class 'NoneType'>

name = "이몽룡"
'''작은 따옴표도
주석으로 사용해도 됨'''

print(name)

####################################################
# 행 분리
# 역슬래시 또는 괄호 사용
a = 1 + 2 + 3 + \
            4 + 5 + 6
b = (1 + 2 + 3 +
                4 + 5 + 6)

print(a)
print(b)

# 여러 줄을 출력할 땐 줄바꿈 문자 (\n) 사용
print("첫째 줄 \n둘째 줄 \n셋째 줄")

string = "홍길동\n010-1234-1234\n서울시 강남구"
print(string)

string = "홍길동\t010-1234-1234\t서울시 강남구"
print(string)

# 특수문자로 해석하지 않도록 특수문자 의미 없애기
# 첫 번째 따옴표 앞에 r 추가
print(r"C:\info\name")

# print() 함수 연속 사용
print("홍길동"); print("홍길동")

# 옆으로 출력
print("first", end=" ") # 스페이스
print("second")

print("first", end="-") # 구분자 -
print("second")