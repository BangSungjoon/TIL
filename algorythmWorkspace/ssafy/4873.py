# 16467. 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기
T = int(input())

for test_case in range(1, T+1):
    string = input()
    new_string = []
    for s in string:
        if new_string == [] or new_string[-1] != s:
            new_string.append(s)
        else:
            new_string.pop()

    print(f'#{test_case} {len(new_string)}')