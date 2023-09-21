# split() 메소드
string = 'Python Programming'
string_split = string.split()
print(string_split) # 리스트로 반환

name = '홍길동, 이몽룡, 성춘향, 변학도'
name_split = name.split(',') # 구분자 : ,
print(name_split)

colors = 'red:blue:yellow:green'
colors_split = colors. split(':')
print(colors_split)

# 리스트의 각 요소 출력
for color in colors_split:
    print(color)

# 문자열인 경우 출력 확인
for color in colors:
    print(color)

# range() 사용 : 인덱스로 출력
for i in range(0, len(colors_split)):
    print(colors_split[i])

print(len(colors_split))
