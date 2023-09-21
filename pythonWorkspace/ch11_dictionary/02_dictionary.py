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

# keys(), values(), items() 메소드
print(naver.keys())    # key 리스트
print(naver.values())  # value 리스트
print(naver.items())   # (key, value) 리스트
# dict_keys(['name', 'url', 'userID', 'password'])
# dict_values(['naver', 'www.naver.com', 'nv', '1234'])
# dict_items([('name', 'naver'), ('url', 'www.naver.com'), ('userID', 'nv'), ('password', '1234')])

# keys(), values(), items() 메소드 타입
print(type(naver.keys()))    # <class 'dict_keys'>
print(type(naver.values()))  # <class 'dict_values'>
print(type(naver.items()))   # <class 'dict_items'>

# 리스트로 변환 : list() 함수 사용
to_list = list(naver.keys())
print(to_list)    # ['name', 'url', 'userID', 'password']
print(type(to_list))

# 튜플로 변환 : tuple() 함수 사용
to_tuple = tuple(naver.keys())
print(to_tuple)   # ('name', 'url', 'userID', 'password')
print(type(to_tuple))

#####################################################

# 각 요소 출력
for key in naver.keys():
    print(key)

print()

for value in naver.values():
    print(value)

print()

for item in naver.items():
    print(item)

# key로 value 찾기
print(naver['userID']) # nv
# get() 메소드 사용해서 찾기
print(naver.get('password')) # 1234

# 존재하지 않는 경우
# print(naver['link']) # 존재하지 않으면 오류 : KeyError
print(naver.get('link')) # None
print(naver.get('link', '없음')) # 없을 경우 '없음' 출력

# 반환값이 None 인 경우 처리
insert_key = 'link'
if naver.get(insert_key) is None:
    print(insert_key + '에 대한 data가 없습니다')



# 존재 여부만 확인 : in / not in
print('link' in google)      # False
print('link' not in google)  # True

###############################################
# 딕셔너리 합치기
# (1) update() 메소드 사용
# (2) ** 연산자 사용

# (1) update() 사용 : 원래의 값 없어지고 병합 결과만 남음
dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}

# dict1에 dict2가 합쳐져서 dict1에 덮어씀
dict1.update(dict2)
print(dict1) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dict2) # {'c': 3, 'd': 4}

dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}
# dict2에 dict21 합쳐져서 dict2에 덮어씀
dict2.update(dict1)
print(dict1) # {'a': 1, 'b': 2}
print(dict2) # {'c': 3, 'd': 4, 'a': 1, 'b': 2}

# (2) ** 사용 : 원래 딕셔너리에 영향을 미치지 않음
dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}
dict3 = {**dict1, **dict2}
print(dict1) # {'a': 1, 'b': 2}
print(dict2) # {'c': 3, 'd': 4}
print(dict3) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

dict4 = {**dict2, **dict1}
print(dict4) # {'c': 3, 'd': 4, 'a': 1, 'b': 2}