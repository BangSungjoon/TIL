# 내장 함수
print('-----abs()-----')

# abs(x) : x의 절대값 반환
print(abs(-10)) # 10

print('-----chr()-----')

# chr(int) : 아스키 코드값에 해당되는 문자 반환
print(chr(97)) # a
print(chr(65)) # A
print(chr(13)) # Enter

print('-----ord()-----')

# ord(c) : 문자에 해당되는 아스키 코드값 반환
print(ord('a'))
print(ord('0'))
print(ord('\n'))
print(ord(' '))  # 32
print(ord('\r')) # 13 : Enter

print('\n-----filter()-----')

# filter(function, iterable)
# 함수에 입력되었을 때 반환값이 참인 것만 묶어서(걸러내서) 반환
# 반환값은 filter object
# list() 함수 사용하여 반환값을 리스트로 받아온다.
# filter : 여과기, 거르다, 걸러내다

def positive(x):
    return x > 0 # 양수만 반환

print(filter(positive, [0, -1, 5, -7, 10]))
# <filter object at 0x000002DDF0C8BF10>

print(list(filter(positive, [0, -1, 5, -7, 10])))
# [5, 10]

# filter() 사용해서 짝수만 반환받아서 출력
# [1, 2, 3, 4, 5, 6 , 7, 8]
def even_number(x):
    if x % 2 == 0:
        return x

print(list(filter(even_number, [1, 2, 3, 4, 5, 6, 7, 8])))

# 또는
def even_number(x):
    return x % 2 == 0

print(list(filter(even_number, [1, 2, 3, 4, 5, 6, 7, 8])))

print('\n-----map()-----')

# map(function, iterable)
# iterable 각 요소가 함수 function에 의해 수행된 결과 반환

def increase(x):
    return x + 1

print(map(increase, [1, 2, 3, 4, 5]))              # <map object at 0x00000277A2D47FD0>
print(list(map(increase, [1, 2, 3, 4, 5])))        # [2, 3, 4, 5, 6]
print(tuple(list(map(increase, [1, 2, 3, 4, 5])))) # (2, 3, 4, 5, 6)

# map() 함수를 사용하여 각 원소의 값을 제곱으로 변환
# power()
# [1, 2, 3, 4, 5]
def power(x):
    return x * x
print(list(map(power, [1, 2, 3, 4, 5])))


print('\n-----pow()-----')

# pow(x, y) : x의 y제곱한 결과값 반환
print(pow(10, 3)) # 1000


print('\n-----round()-----')

# round(실수, 소수점 이하 자리수) : 실수를 반올림하여 반환
print(round(3.141592, 2)) # 3.14

print('\n-----zip()-----')

# zip(*iterable) : 각 iterable에서 동일한 인덱스의 요소를 추출하여 묶어서 반환

print(zip([1, 2, 3], [10, 20, 30])) # zip 객체 반환
print(list(zip([1, 2, 3], [10, 20, 30]))) # [(1, 10), (2, 20), (3, 30)]

# zip(리스트, 리스트)
# zip(튜플, 튜플)
# zip(리스트, 튜플)

# 리스트와 튜플 같이 사용
keys = ['apple', 'pear', 'peach']
values = (300, 250, 400)
print(dict(zip(keys, values)))


print('\n-----lambda 식-----')

# 람다식
# 실행 시 생성해서 사용할 수 있는 익명 함수
# 익명 함수 : 이름이 없는 함수
# 입력과 출력이 있는 간단한 한 행의 함수를 만들 때 사용
# 같은 함수를 def 문으로 정의할 때보다 간결
# 형식 : (lambda 매개변수 : 리턴값)(인수)
# (lambda a, b : a + b)(3, 5)

# def로 정의한 함수
def add(a, b):
    return a + b

print(add(3, 5))

# 람다식으로 표현
print((lambda a, b : a + b)(3, 5))

# 매개변수, 반환값 하나라도 없으면 오류
print((lambda a : a)('abc'))

# 람다식의 결과를 변수에 할당하여 재사용 가능
lambda_add = lambda x, y : x + y
print(lambda_add(3, 5))

# 람다식을 map()에 적용
# [1, 2, 3]
# 각 원소의 세제곱값을 반환받아서 리스트로 출력
print(list(map((lambda x : x**3), [1, 2, 3])))