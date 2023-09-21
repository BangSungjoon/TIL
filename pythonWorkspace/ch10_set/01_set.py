# 집합 (Set)

# 빈 집합 생성
s = set()
print(s) # set()
print(type(s)) # <class 'set'>

s1 = {1, 2, 3, 4, 5}
print(s1)
print(type(s1))

# 리스트로 집합 생성
s2 = set([10, 20 ,30])
print(s2) # {10, 20, 30}
print(type(s2))

# 튜플로 집합 생성
s3 = set((100, 200, 300))
print(s3)           # {200, 100, 300}
print(type(s3))     # <class 'set'>

# 동일한 요소(값) 중복될 수 없다
s4 = { 1, 2, 3, 3, 4 } # 오류는 없음
# 중복값을 제거하고 집합 생성
print(s4) # {1, 2, 3, 4}

# 집합 안에 변경 가능한 요소(리스트) 포함할 수 없다
s5 = {1, 2, [3, 4]} # TypeError: unhashable type: 'list'

# unhashable type
# 집합은 모든 요소들을 해싱을 이용하여 저장하고 관리
# 해싱 : 각 객체에 식별할 수 있는 키, 값 (코드)를 부여해서
# 객체를 테이블에 저장하는 방식
# 이 해시 코드가 변경되면 안 되므로 각 요소의 값을 변경할 수 없음

# 집합에 요소 추가
s = {1, 2, 3}
s.add(4)
print(s) # {1, 2, 3, 4}

# 여러 개 추가 시
s.update([5, 6])
print(s) # {1, 2, 3, 4, 5, 6}

# 요소 제거
s.remove(3) # 값3 제거
print(s)    # {1, 2, 4, 5, 6}

s.discard(5) # discard(값)
print(s)     # {1, 2, 4, 6}

# 없는 요소 삭제 시
# s.remove(10) # 오류
s.discard(10)  # 오류 없음

s = {1, 2, 3}
s.clear() # 전체 요소 삭제 (집합 비우기)
print(s)  # set() : 빈 집합

# 완전 삭제
s = {1, 2, 3}
del s
print(s) # NameError: name 's' is not defined