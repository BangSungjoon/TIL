# 13732. 정사각형 판정
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    check = False

    for i in range(N):      # 최소 x, y 값 찾기
        for j in range(N):
            if arr[i][j] == '#':
                min_x = j
                min_y = i
                check = True
                break
        if check:
            break
    check = False
    for i in range(N-1, -1, -1):        # 최대 x, y 값 찾기
        for j in range(N-1, -1, -1):
            if arr[i][j] == '#':
                max_x = j
                max_y = i
                check = True
                break
        if check:
            break
    check = False
    if max_x-min_x == max_y-min_y:  # 가로 세로 길이가 같다면
        for i in range(min_y, max_y+1):
            for j in range(min_x, max_x+1):
                if arr[i][j] == '.':
                    print(f'#{test_case} no')
                    check = True
                    break
            if check:
                break
        else:
            print(f'#{test_case} yes')
    else:
        print(f'#{test_case} no')