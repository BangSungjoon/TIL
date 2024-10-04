# 2805. 농작물 수확하기
T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [input() for _ in range(n)]
    result = 0  # 수익

    if n == 1:
        result = int(arr[0][0])
        print(f'#{test_case} {result}')
        continue

    for i in range(n):
        if i <= n//2:   # 절반 전 까진
            for j in range(n//2-i, n//2+i+1):
                result += int(arr[i][j])
        else:           # 절반 이후부터는
            for j in range(i-n//2, n-(i-n//2)):
                result += int(arr[i][j])

    print(f'#{test_case} {result}')