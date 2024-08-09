def f(i, N):    # i 현재 인덱스, N 크기
    if i==N:    # 배열을 벗어난 경우
        return
    else:
        print(arr[i])
        f(i+1, N)
        return

arr = [1, 2, 3]
N = 3
f(0, N)