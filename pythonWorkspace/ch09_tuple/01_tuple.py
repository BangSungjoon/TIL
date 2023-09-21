t2 = tuple()
print(t2)

t3 = (1, 2, 3)
print(t3)

t4 = 4, 5, 6
print(t4)

t5 = [1, 2], [3, 4] # 리스트로 튜플 생성
print(t5) # ([1, 2], [3, 4])

t3 = (1, 2, 3)
t6 = t3, (7, 8, 9) # 다른 튜플 포함 가능
print(t6) # ((1, 2, 3), (7, 8, 9))

t7 = tuple([5, 6, 7, 8]) # tuple() 함수 사용
print(t7)

print(type(t7)) # <class 'tuple'>

# 튜플 생성 시 주의
# 숫자 1만 포함된 튜플 생성
t = (1,)
print(t) # (1,)
print(type(t)) # <class 'tuple'>

# (1)만 적으면 튜플이 아니라 정수 1이 저장된 int 타입
t = (1)
print(t) # (1)
print(type(t)) # <class 'int'>

# 튜플을 리스트로 변환
t3 = (1, 2, 3)
to_list1 = list(t3)
print(to_list1) # [1, 2, 3]