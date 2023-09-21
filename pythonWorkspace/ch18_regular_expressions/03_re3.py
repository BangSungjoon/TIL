# 반복을 나타내는 메타 문자
# + : 최소 1번 이상
# * : 최소 0번 이상

import re
string = "Thoe are my books writen by Mr. Kook."

result = re.findall('o', string)
print(result) # ['o', 'o', 'o', 'o', 'o']

# + : 최소 1번 이상 (단어 단위)
import re
string = "Thoe are my books writen by Mr. Kook."

result = re.findall('o+', string)
print(result) # ['o', 'oo', 'oo']

# * : 최소 0번 이상 (단어 단위)
import re
string = "Thoe are my books writen by Mr. Kook."

result = re.findall('o*', string)
print(result) 

# {1, 5} : 1 ~ 5회 반복
import re
string = "Thoe are my books writen by Mr. Koooook."

result = re.findall('o{1,5}', string)
print(result) # ['o', 'oo', 'ooooo']

# {1, } : 최소 1회 이상 반복하고 다음에 k
import re
string = "Thoe are my books writen by Mr. Koooook."

result = re.findall('o{1,}k', string)
print(result) # ['ook', 'oooook']