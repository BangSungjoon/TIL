# isalpha() / isdigit() / isspace()
# 문자/숫자/공백 여부 확인 메소드

phone = input('전화번호 입력 (숫자만) : ')

if phone.isdigit():
    pass
else:
    print('숫자만 입력하세요')

print('입력한 값 : ', phone)

####################################################
name = input('이름 입력 : ')

# 문자가 아닌 경우
if not(name.isalpha()):
    print('문자만 입력하세요')

print('입력한 값 : ', name)

####################################################
id = input('ID 입력 : ')

# 문자 또는 숫자가 아닌 경우
if not(id.isalnum()):
    print('문자와 숫자만 입력할 수 있습니다')

print('입력한 값 : ', id)

####################################################
# 스페이스 여부 확인
print(' '.isspace()) # 1개 문자의 경우 : True
print(' c'.isspace()) # 2개 이상의 문자의 경우 : False