# 예외 처리 : 에러 확인

# ZeroDivisionError : 0으로 나눈 경우 발행
print(10/0)

# TypeError : 문자 + 숫자 인 경우 : 형변환 필요
print('나이 : ' + 23 + '살 ')

# NameError : 변수 정의되어 있지 않음. 변수명 인식 불가
# print(x)

# ValueError : 포맷 오류
c = 100
print('%d%' %c) # 퍼센트 %%

# SyntaxError : 구문 오류 (: 콜론 빠짐)
# if c > 80
#     print('합격')