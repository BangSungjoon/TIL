def check(check_list):
    if check_list == '0001101':
        return 0
    elif check_list == '0011001':
        return 1
    elif check_list == '0010011':
        return 2
    elif check_list == '0111101':
        return 3
    elif check_list == '0100011':
        return 4
    elif check_list == '0110001':
        return 5
    elif check_list == '0101111':
        return 6
    elif check_list == '0111011':
        return 7
    elif check_list == '0110111':
        return 8
    elif check_list == '0001011':
        return 9

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    hollsoo = 0
    zzacksoo = 0

    # 암호 코드 찾기
    for i in range(N):
        if '1' in arr[i]:
            for j in range(-1, -M-1, -1):
                if arr[i][j] == '1':  # 암호문이 시작되는 점을 만나면
                    bit = arr[i][j-55:j+1]
                    break
            break

    # 7개씩 끊어서 비트로 변환
    password = [0]*8        # 암호코드는 8개의 숫자
    for i in range(8):
        password[i] = bit[7*i:7*i+7]
        password[i] = check(password[i])
        if i % 2 == 0:
            hollsoo += password[i]
        else:
            zzacksoo += password[i]
    # 올바른 암호코드인지 검사
    result = (hollsoo*3)+zzacksoo
    if result % 10 != 0:
        result = 0
    else:
        result = hollsoo + zzacksoo
    print(f'#{test_case} {result}')