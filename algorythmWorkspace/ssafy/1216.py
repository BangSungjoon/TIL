# 회문 2
T = 10

for test_case in range(1, T+1):
    num = int(input())
    N = 100
    # M = 1부터 100까지
    arr = [list(input()) for _ in range(N)]
    max_len_pal = 1

    for M in range(2, 101):             # 회문의 길이 2부터 100까지 전부 검사
        for i in range(N):              # 가로 세로 N개의 줄이니 N번만큼 반복
            for j in range(N-M+1):      # 각 줄당 패턴 검색해야 할 횟수 N-M
                row = arr[i][j:j+M]     # 가로줄 검사문장 인덱싱 j부터 j+M까지
                col = [arr[k][i] for k in range(j, j+M)]    # 세로줄은 인덱싱이 안되기에 리스트를 생성하여 넣어준다.

                if row == row[::-1]:    # 만약 회문이라면
                    max_len_pal = M     # 최대 길이는 회문의 길이 M이 된다.
                if col == col[::-1]:    # 세로줄도 마찬가지!
                    max_len_pal = M
    print(f'#{num} {max_len_pal}')