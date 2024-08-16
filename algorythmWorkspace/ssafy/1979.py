# 1979. 어디에 단어가 들어갈 수 있을까
T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())    # N: 단어 퍼즐 사이즈, K: 특정 단어 길이
    word_arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        r_cnt = 0
        c_cnt = 0
        for j in range(N):
            # 가로 검사
            if word_arr[i][j] == 1:       # 흰색 부분이라면
                r_cnt += 1                # 한칸 추가욧
            else:
                if r_cnt == K:            # 검은 부분을 만났는디 이때까지의 길이가 K라면
                    result += 1           # 정답 수 하나 추가욧
                r_cnt = 0                 # 지금까지 센 칸 수 초기화
            # 세로 검사 드가자
            if word_arr[j][i] == 1:
                c_cnt += 1
            else:
                if c_cnt == K:
                    result += 1
                c_cnt = 0
        if r_cnt == K:
            result += 1
        if c_cnt == K:
            result += 1

    print(f'#{test_case} {result}')