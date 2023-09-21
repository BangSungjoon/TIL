# 파일 읽기 : readlines()로 전체 파일 읽기

# 1개 행이 리스트의 요소
# 행 끝에 \n 포함되어 있음
f1 = open('test.txt', 'r', encoding='utf-8')
line = f1.readlines()
print(line) # 리스트로 생성
f1.close()

# 전체 라인 읽어서 1행씩 출력
f2 = open('test.txt', 'r', encoding='utf-8')

while True:
    line = f2.readlines()
    if not line:
        break
    print(line, end='') # 1행 출력하고 줄바꿈. 행 간격 있음

f2.close()