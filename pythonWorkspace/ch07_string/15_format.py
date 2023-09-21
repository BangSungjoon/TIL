# 문자열 정렬 : 정렬 문자 사용 (<, >, ^)
string = 'python'

print('{0:<10}'.format(string)) # 전체 10자리 왼쪽 정렬
print('{0:>10}'.format(string)) # 전체 10자리 오른쪽 정렬
print('{0:^10}'.format(string)) # 전체 10자리 가운데 정렬

# 공백 문자 지정 : -로 지정 시 (공백대신 -로 출력)
print('{0:-^10}'.format(string))

# ljust(), center(), rjust() 사용해서 정렬
print(string.ljust(10))
print(string.center(10))
print(string.rjust(10))

# 공백 문자 지정
print(string.rjust(10, '-'))
print(string.center(10, '-'))

# f-string 정렬
string = 'python'
print(f'{string:>10}')
print(f'{string:<10}')