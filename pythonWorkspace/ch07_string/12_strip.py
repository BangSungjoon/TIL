# strip() / lstrip() / rstrip()

a = '   hello   '
print(a)
print(a.strip())    # 문자열 앞 뒤의 공백 제거 (양쪽 다 제거)
print(a.lstrip())   # 문자열의 왼쪽 공백 제거
print(a.rstrip())   # 문자열의 오른쪽 공백 제거

id = 'sun'
input_id = '  sun'
if id == input_id.strip():
    print('로그인 성공')
else:
    print('로그인 실패')