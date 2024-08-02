# 16354. 4865. 글자수
T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    max_cnt = 0

    for char in str1:
        cnt = 0
        for target in str2:
            if char == target:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    print(f'#{test_case} {max_cnt}')