# 부분집합의 합
T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    answer = 0

    for i in range(1 << 12):    # 모든 부분 집합을 체크 (2**12)
        N_count = 0             # 부분집합의 원소의 개수
        sub_sum = 0             # 부분집합의 합
        for j in range(12):     # 각 부분집합마다 순회
            if i & (1 << j):    # 만약 i의 j번째 위치가 1이라면
                N_count += 1    # 부분집합의 원소의 개수 1 증가
                sub_sum += j+1  # 원소만큼 합 증가
                if N_count > N or sub_sum > K: # 만약 부분집합의 원소의 수나 합이 N과 K보다 커진다면 즉시 종료
                    break
        if sub_sum == K and N_count == N:   # 이 부분집합이 조건에 맞는다면
            answer += 1                     # 정답 1 증가

    print(f'#{test_case} {answer}')
