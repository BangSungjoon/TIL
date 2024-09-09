# 순회하며 누적 점수 구하는 함수 ( DFS )
def check_scores(score_li: list, lined: list, N: int, idx_now: int, hap: int = 0):
    # 줄에 서있다는 기록 리스트의 해당 인덱스 위치에 남기기
    lined[idx_now] = 1

    # CASE 1 : 만약 모두 줄에 선 경우 -> 대소 비교를 통한 변수 할당
    if sum(lined) == N:
        # 직전 최소 점수와 비교하여 점수 재할당
        global scores_min
        if scores_min > hap:
            scores_min = hap

    # CASE 2 : 아직 줄 서야 하는 인원이 남은 경우
    else:
        # 하나씩 순회하며 비교하기
        for idx_next in range(N):
            # 줄에 서지 않은 경우, 줄 세우며 확인하기 ( 인덱스 값 재조정 및 점수 더해준 후, 함수 재실행 )
            if not lined[idx_next]:
                check_scores(score_li, lined, N, idx_next, hap + score_li[idx_now][idx_next])

    # 다른 케이스를 위해 기록 삭제 ( 다른 조합 순서 케이스를 위해 줄에서 빼기 )
    lined[idx_now] = 0

## 실행 ##
for t in range(int(input())):
    # 변수 입력 받기
    N = int(input())
    danger_scores = [list(map(int, input().split())) for _ in range(N)]

    # 하나씩 순회하며 함수를 실행하고, 최소 점수 확인하기
    scores_min = 9999999999  # 최저 점수 변수 초기화
    for i in range(N):
        check_scores(danger_scores, [0] * N, N, i)  # 순회를 통한 확인 ( 시작 인덱스 변경 위해 for문으로 순회 )

    print(f"#{t + 1} {scores_min}")