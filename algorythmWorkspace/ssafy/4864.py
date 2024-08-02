# 16331. 4864. 문자열 비교
T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    result = 0

    for i in range(len(str2)-len(str1)+1):
        if str2[i:i+len(str1)] == str1:
            result = 1
    print(f'#{test_case} {result}')