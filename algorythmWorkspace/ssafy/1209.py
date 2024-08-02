for test_case in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 각 줄의 합 구하기
    dia_1 = 0
    dia_2 = 0
    lst = []

    for i in range(100):
        row = 0
        col = 0
        for j in range(100):
            row += arr[i][j]
            col += arr[j][i]
            if i == j:
                dia_1 += arr[i][j]      # 대각선1
            if 99-i == j:
                dia_2 += arr[99-i][j]   # 대각선2
        lst.append(row)
        lst.append(col)
    lst.append(dia_1)
    lst.append(dia_2)

    # 최댓값 구하기
    max_sum = 0
    for a in lst:
        if a >= max_sum:
            max_sum = a
    print(f'#{test_case} {max_sum}')