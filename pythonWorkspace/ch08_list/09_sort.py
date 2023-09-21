# 리스트 정렬 : sort() / sorted() / reverse()

# sort() 메소드 : 리스트 정렬. 기본 오름차순 정렬
# 원본 리스트 변경됨
scores = [90, 78, 81, 64, 89]
scores.sort() # [64, 78, 81, 89, 90] : 기본 오름차순 정렬
print(scores) # 원본 변경됨

scores = [90, 78, 81, 64, 89]
scores.sort(reverse=True) # 내림차순 정렬 : [90, 89, 81, 78, 64]
print(scores) # 원본 변경됨

scores = [90, 78, 81, 64, 89]
scores.reverse() # [89, 64, 81, 78, 90] : 역순으로 변경 () (정렬은 안 함)
print(scores)

# 영문자는 대문자 앞으로, 소문자 뒤로 정렬됨
char = ['b', 'A', 'd', 'C']
char.sort()
print(char) # ['A', 'C', 'b', 'd']

# 대소문자 구별없이 정렬
# key 매개변수에 str.lower 지정
char = ['b', 'A', 'd', 'C']
char.sort(key=str.lower)
print(char) # ['A', 'b', 'C', 'd']

# 대소문자 구별없이 역순으로 정렬
char = ['b', 'A', 'd', 'C']
char.sort(key=str.lower, reverse=True)
print(char) # ['d', 'C', 'b', 'A']

# 문자열은 첫 문자로 정렬됨 (대문자 먼저 소문자 나중에)
ids = ['SKY', 'Blue', 'red', 'eBook', 'GREEN', 'blue']
ids.sort()
print(ids) # ['Blue', 'GREEN', 'SKY', 'blue', 'eBook', 'red']

# 대소문자 구별없이 정렬
ids = ['SKY', 'Blue', 'red', 'eBook', 'GREEN', 'blue']
ids.sort(key=str.lower)
print(ids) # ['Blue', 'blue', 'eBook', 'GREEN', 'red', 'SKY']

# sorted() 내장 함수 : 원본 유지하면서 정렬된 새로운 리스트 반환
a = [3, 5, 2, 1, 4]
b = sorted(a)
print('a :', a) # a : [3, 5, 2, 1, 4] (원본 유지)
print('b :', b) # b : [1, 2, 3, 4, 5] (정렬된 리스트)