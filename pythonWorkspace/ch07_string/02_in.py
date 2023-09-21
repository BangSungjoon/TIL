# in / not in : 포함 여부
string = 'Python Programming'

print('python' in string) # True
print('programming' in string) # False (대소문자를 구분하기 때문)

if 'python' in string:
    print('있음')
else:
    print('없음')