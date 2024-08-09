# 16332. 4861. 회문
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):              # 가로 세로 N개의 줄이니 N번만큼 반복
        for j in range(N-M+1):      # 각 줄당 패턴 검색해야 할 횟수 N-M
            row = arr[i][j:j+M]     # 가로줄 검사문장 인덱싱 j부터 j+M까지
            col = [arr[k][i] for k in range(j, j+M)]    # 세로줄은 인덱싱이 안되기에 리스트를 생성하여 넣어준다.

            if row == row[::-1]:    # 만약 회문이라면
                row = ''.join(row)  # 리스트 문장으로 합치기
                print(f'#{test_case} {row}')    # 출력
            if col == col[::-1]:    # 세로줄도 마찬가지!
                col = ''.join(col)
                print(f'#{test_case} {col}')
