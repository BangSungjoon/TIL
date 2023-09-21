# + : 최소 1번 이상
# 문자 연결 (단어 단위의 리스트 반환)
import re
string = "ID seoul_777 lived in Seoul in 2015"

result = re.findall('[a-z]+', string) # 소문자
print(result)

import re
string = "ID seoul_777 lived in Seoul in 2015"

result = re.findall('[A-Z]+', string) # 대문자
print(result)

import re
string = "ID seoul_777 lived in Seoul in 2015"

result = re.findall('[a-zA-Z]+', string) # 대문자 소문자
print(result)

# ^ : not(포함되지 않은)
import re
string = "ID seoul_777 lived in Seoul in 2015"

result = re.findall('[^0-9]', string) # 숫자 포함되지 않은
print(result)