# 18131. 0802. 부분집합의 합
T = int(input())

for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))
    result = 0
    for i in range(1 << 10):
        sub_sum = 0
        answer = False
        for j in range(10):
            if i & (1 << j):
                sub_sum += numbers[j]
                answer = True
        if sub_sum == 0 and answer == True:
            result = 1
            break

    print(f'#{test_case} {result}')