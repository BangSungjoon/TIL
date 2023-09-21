# 기존 파일 내용 덮어쓰지 않고
# 파일 끝에 새로 추가
# 파일 열기 모드 : a
# append

f = f = open('test2.txt', 'a', encoding='utf-8')
append_data = '\n\nPython Programming'
f.write(append_data)

# 파일 읽어서 추가된 내용 확인
f = open('test2.txt', 'r', encoding='utf-8')
print(f.read())

f.close()