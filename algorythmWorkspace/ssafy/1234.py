# 1234. [S/W 문제해결 기본] 10일차 - 비밀번호
for test_case in range(1, 11):
    N, number = input().split()
    password = [number[0]]

    for i in range(1, int(N)):
        if password == [] or password[-1] != number[i]:
            password.append(number[i])
        else:
            password.pop()
    print(f'#{test_case}', end=' ')
    for num in password:
        print(num, end='')
    print()