# 파일 읽기 : readline() 메소드를 이용해서 1개 라인 읽어 오기

# 첫 번째 행 읽기
f1 = open('test.txt', 'r', encoding='utf-8')
line = f1.readline()
print(line) # 안녕하세요, 홍길동 입니다.
f1.close()

# readline() 사용해서 파일 전체 읽기
f2 = open('test.txt', 'r', encoding='utf-8')

while True:
    line = f2.readline()
    if not line:
        break
    print(line) # 1행 출력하고 줄바꿈. 행 간격 있음

f2.close()

# 행 간격 제거
f2 = open('test.txt', 'r', encoding='utf-8')

while True:
    line = f2.readline()
    if not line:
        break
    print(line, end='') # 1행 출력하고 줄바꿈. 행 간격 있음

f2.close()