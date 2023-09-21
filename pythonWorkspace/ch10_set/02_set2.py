# 집합 연산

A = {1, 2, 3}
B = {3, 4, 5}

# 합집합
C = A | B
print(C) # {1, 2, 3, 4, 5} 중복값 제거됨

C = A.union(B)
print(C) # {1, 2, 3, 4, 5} 

# 교집합
A = {1, 2, 3}
B = {3, 4, 5}

C = A & B
print(C) # {3}

C = A.intersection(B)
print(C) # {3}

# 차집합
A = {1, 2, 3}
B = {3, 4, 5}

C = A - B
print(C) # {1, 2}

C = A.difference(B)
print(C) # {1, 2}