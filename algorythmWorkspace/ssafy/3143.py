T = int(input())

for test_case in range(1, T+1):
    A, B = input().split()
    idx, cnt = 0, 0  # idx : A의 인덱스 슬라이싱을 위한 인덱스, cnt : B가 몇번 등장했는지 세는 변수
    while idx < len(A):     # A의 길이를 넘어가지 않는다면 반복
        if A[idx:idx+len(B)] == B:  # 현재 위치부터 B의 글자 수 만큼 슬라이싱 했을 때 B와 일치한다면
            cnt += 1                # B의 등장 횟수 1증가
            idx += len(B)           # 인덱스 옮겨주기
        else:
            idx += 1                # 일치하지 않는 다면 다음 칸 검사
    result = len(A) - len(B) * cnt + cnt    # 원래 A의 글자 수에서 (B의 글자 수)x(등장횟수) 만큼 빼주고 등장 횟수 더해주기
    print(f'#{test_case} {result}')