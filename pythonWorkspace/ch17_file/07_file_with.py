# with 문 사용 파일 열기

# 쓰기 모드
with open('file9.txt','w', encoding='utf-8') as f:
    f.write('with 사용해서 파일에 쓰기')

# 변수로 처리
file = 'file10.txt'
data = '''--Python Programming
Database
Django'''

# 쓰기 모드
with open(file, 'w', encoding='utf-8') as f:
    f.write(data)

# 읽기 모드
with open(file, 'r', encoding='utf-8') as f:
    print(f.read())