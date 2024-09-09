# 5658. [모의 SW 역량테스트] 보물상자 비밀번호
T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    box = input()
    password = set()        # 나올 수 있는 비밀번호 담아둘 set
    len_password = N // 4   # 각 비밀번호의 길이

    for _ in range(len_password):       # 회전 드가자
        for j in range(4):              # 1회전당 4개의 비밀번호가 나오니깐
            num = ''                    # 각 번호를 담을 빈 문자열 생성
            for k in range(len_password):
                num += box[j*len_password + k]
            num = int(num, 16)          # 16진수 10진수로 변환
            password.add(num)           # password 배열에 더해주기
        temp = box[-1]                  # 문자열 맨 끝값 담기
        box = temp + box[:-1]           # 문자열 재조정

    password = sorted(password, reverse=True)
    print(f'#{test_case} {password[K - 1]}')
