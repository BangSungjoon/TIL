# 구구단 옆으로 출력
for i in range(1, 10):
    for j in range(2, 10):
        print(f'{j} * {i} = {i*j}', end='\t')
    print()