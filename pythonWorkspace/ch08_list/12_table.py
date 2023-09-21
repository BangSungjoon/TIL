# 2차원 리스트 : 테이블 형태
table = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15]]

print(table)
# [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

print('-----------------------------------------------')

table = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15]]

# 1행씩 출력
for row in table:
    print(row)

# 각 리스트 안의 원소 출력
for row in table:
    for j in row:
        print(j, end='\t')
    print()


table = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15]]
# table[행][열] 방식으로 출력
rows = len(table) # 행의 수
cols = len(table[0]) # 열의 수
print(rows, cols)

for r in range(rows):
    for c in range(cols):
        print(table[r][c], end='\t')
    print()

# 리스트의 각 행의 열의 개수가 다른 경우 각 원소 출력
table = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10, 10],
         [11, 12, 13, 14]]


for row in range(len(table)):
    for col in range(len(table[row])):
        print(table[row][col], end='\t')
    print()
