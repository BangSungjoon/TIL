# 이메일 유효성 확인
# 이메일 형식
# - 시작 문자와 숫자가 2개 이상 @문자와 숫자가 2개이상.문자 2개이상 끝
# ^ : 시작
# $ : 끝
# \. : 점(dot) 특수문자 (.), (.)만 써도 됨
import re
email = input('이메일 입력 : ')
result = re.findall('^[a-zA-Z0-9]{2,}@[a-zA-Z0-9]{2,}\.[a-z]{2,}$', email)

print(email, end=' ')

if(len(result) == 0):
    print('잘못된 이메일 형식')
else:
    print('올바른 이메일 형식')