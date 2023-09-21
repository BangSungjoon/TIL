# read() 사용하여 파일 읽기
# 내용 전체를 읽어서 1개의 문자열로 반환
f = open('test2.txt','r',encoding='utf-8')
data = f.read()
print(data)
print(type(data))
print(len(data))

# 1개 문자씩 출력
for ch in data:
    print(ch)

# 파일 내에서 검색
f = open('test2.txt', 'r', encoding='utf-8')
data = f.read()

value = input('검색값 입력 : ')

# 문자열에 검색 값이 있는지 확인
if value in data:
    print('있음')
else:
    print('없음')

f.close()