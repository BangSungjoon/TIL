# \d : 숫자 ([0-9]와 동일)
import re
string = "ID seoul_777 lived in Seoul in 2015"

result = re.findall('[\d]', string) # 숫자 포함되지 않은
print(result)

# \s : 스페이스
import re
string ='ID seoul_777 lived in Seoul in 2015'

result = re.findall('[\s]', string) 
print(result)

# \W: 문자 + 숫자 (alphanumeric)가 아닌 것 ([^a-zA-Z0-9_]와 동일)
import re
string ='ID seoul_777 lived in Seoul in 2015'

result = re.findall('[\W]', string) 
print(result)

# 문자 + 숫자 형태만 추출 : ['seoul_777', '2015']
import re
string ='ID seoul_777 lived in Seoul in 2015'

result = re.findall('[\w]+[\d]', string) 
print(result)