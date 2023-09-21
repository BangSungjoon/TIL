# 모듈 전체 참조
import new_calculator

# new_calculator을 통해서 함수 접근
result = new_calculator.add(3, 7)
print(result) # 10

# 모듈 내 함수 직접 참조
from new_calculator import sub

result1 = sub(7, 4)
print(result1)

# add()는 new_calculator 통해서 호출 가능
result2 = new_calculator.add(7, 4)

# (3) 모듈 내 모든 함수 참조
from new_calculator import *

a = add(7, 4)
s = sub(7, 4)
m = mul(7, 4)
d = div(7, 4)