# 딕셔너리 생성

# (1) { } 중괄호 안에 키:값 형식으로 저장
# 딕셔너리 = {키1:값1, 키2:값2, ...}
scores = {'kor':90, 'eng':88, 'math':95}
print(scores)        # {'kor': 90, 'eng': 88, 'math': 95}
print(type(scores))  # <class 'dict'>

# (2) 빈 딕셔너리 생성 : {} 만 지정
# 딕셔너리 = {}
# 요소 추가 : 딕셔너리[키] = 값
students = {}
students['name'] = '홍길동'
students['age'] = 23
print(students) # {'name': '홍길동', 'age': 23}

# 키 값이 숫자인 경우
nums = {}
nums[1] = 10
nums[2] = 20
nums[3] = 30
print(nums)     # {1: 10, 2: 20, 3: 30}

# (3) dict() 함수 사용
person = dict()
print(person)   # {}
person['이름'] = '홍길동'
person['키'] = 170
person['몸무게'] = 75
print(person)  # {'이름': '홍길동', '키': 170, '몸무게': 75}

person2 = dict(이름='이몽룡', 키=175, 몸무게=80)
print(person2) # {'이름': '이몽룡', '키': 175, '몸무게': 80}

# zip() 함수 사용 : dict(zip([key],[value]))
person3 = dict(zip(['이름', '키', '몸무게'], ['성춘향', 160, 60]))
print(person3) # {'이름': '성춘향', '키': 160, '몸무게': 60}

# 참고 : zip() 함수
# 동일 개수로 이루어진 iteralbe 객체를 인자로 받아서
# 순서대로 각 원소를 튜플의 형태로 반환
# iterable : 반복 가능한 (하나씩 순외 가능한)
numbers = [1, 2, 3]
names = ['홍길동', '이몽룡', '성춘향']
for pair in zip(numbers, names):
    print(pair)

########################################################

# 딕셔너리 생성
d = {1: 'a'}
print(d)   # {1: 'a'}

# 두 번째 요소 추가
d[2] = 'b' # 주의: 2는 인덱스 아님. 키
print(d)   # {1: 'a', 2: 'b'}

member = {'name':'홍길동', 'phone':'010-1234-1234'}
print(member) # {'name': '홍길동', 'phone': '010-1234-1234'}

# 'address : 서울' 추가
member['address'] = '서울'
print(member) # {'name': '홍길동', 'phone': '010-1234-1234', 'address': '서울'}

# 요소가 많아서 길면 여러 줄로 입력해도 됨
naver = {
    'name':'naver',
    'url':'www.naver.com',
    'userID':'nv',
    'password':'1234'
}

google = {
    'name':'google',
    'url':'www.google.com',
    'userID':'gg',
    'password':'5678'
}

print(naver)
print(google)