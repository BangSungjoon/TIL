data = 'hi'
f = open('file4.txt', 'w')
f.write(data)
f.close()

data = '안녕'
f = open('file5.txt', 'w')
f.write(data) # 한글 깨짐 : 인코딩이 ANSI로 되어 있기 때문
f.close()

data = '안녕'
f = open('file6.txt', 'w', encoding='utf-8')
f.write(data) 
f.close()

# 여러 행으로 쓰기
f = open('file7.txt', 'w', encoding='utf-8')

for i in range(1, 11):
    data = "%d행\n" % i
    f.write(data)
f.close()

# str(i) 사용
f = open('file7.txt', 'w', encoding='utf-8')

for i in range(1, 11):
    data = str(i) + "행\n"
    f.write(data)
f.close()