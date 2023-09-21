# 리스트 복사
# 얕은 복사 : 실제 리스트는 새로 생성하지 않고 참조값(주소)만 복사
# 복사본 요소 변경하면 원본 리스트 요소의 값도 변경

scores = [10, 20, 30, 40]
copies = scores

copies[0] = 100  # 복사본을 변경했는데

print(scores)    # 원본도 변경됨 [100, 20, 30, 40]
print(copies)    # [100, 20, 30, 40]

# 깊은 복사 : 새로 생성하여 반환
# 복사본 변경해도 원본 리스트의 원소 값은 변경되지 않음
# list() / deepcopy() 함수 사용
scores = [10, 20, 30, 40]
copies = list(scores)

copies[0] = 100 # 복사본 변경 (원본 변경되지 않음)

print(scores) # [10, 20, 30, 40]
print(copies) # [100, 20, 30, 40]

# deepcopy() 함수 사용
# copy 모듈 import
import copy
a = ['a', 'b', 'c']
b = copy.deepcopy(a)

b[0] = 1 # 복사본 변경 (원본 변경되지 않음)
print(a) # ['a', 'b', 'c']
print(b) # [1, 'b', 'c']