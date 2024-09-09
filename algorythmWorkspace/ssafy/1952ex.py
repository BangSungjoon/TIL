import sys
sys.stdin = open('input.txt', 'r')

# 시작점: 1월 / 누적금액: 0원
# 끝점: 12월
def dfs(month, sum_cost):
    global ans
    # 기저조건. 12월까지 모두 보았는가?
    if month > 12:
        ans = min(ans, sum_cost)
        return

    # 1일권으로 모두 구매 (다음 재귀: 다음 달을 확인)
    dfs(month + 1, sum_cost + (days[month] * cost[0]))

    # 1달권 구매 (다음 재귀: 다음 달을 확인)
    dfs(month + 1, sum_cost + cost[1])

    # 3달권 구매 (다음 재귀: 3달 후를 확인)
    dfs(month + 3, sum_cost + cost[2])

    # 1년권 구매 (다음 재귀: 12달 후를 확인)
    #   - [참고] 사실 재귀에서 빼고, 1월에 구입한 비용이랑 비교해도 된다!
    #   - 직관적으로 보기 위해 강의용으로 추가
    dfs(month + 12, sum_cost + cost[3])

T = int(input())

for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    # 인덱스 너무 헷갈려! 나는 1~12를 쓸거야!
    # 맨 앞에 쓰레기 값 추가
    days = [0] + list(map(int, input().split()))
    ans = 1e9
    dfs(1, 0)
    print(f'#{tc} {ans}')

# -----------------------------------------------------

# 접근 방법2
# 3월 기준으로 생각: 2월 까지의 최소 금액 + 본인의 금액 중 최소 금액
# 이전의 최소 금액들을 활용해서 내 최소금액을 구할 수 있다!
# DP 활용하기
# 왜 DP로 활용 가능 한가?
# 1. 작은 문제로 분할 가능해야한다.
#   - 전체 문제의 합 = 각 달까지의 최소 금액들이 쌓여서 완성
#   -> 각 달까지의 최소 금액 문제로 생각
# 2. 뒤에 결과를 구할 때, 앞에서 구했던 결과가 변하면 안된다.

T = int(input())

for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    days = [0] + list(map(int, input().split()))
    dp = [0] * 13   # 1~12월 최소 금액들을 저장

    for i in range(1, 13):
        # 현재 달의 최소 비용을 계산
        # 1~2월 까지는 이전 달 + 1일권 구입 / 이전 달 + 1달권
        # 이전 달 + 1일권 구입 / 이전 달 + 1달권 / 3달 전에 3달권 구입 중 최소
        dp[i] = min(dp[i - 1] + (days[i] * cost[0]), dp[i - 1] + cost[1])

        # index 오류를 피하기 위해, 3월 이후 계산을 따로 작성
        if i >= 3:
            # 1일권 vs 1달권 vs 3달권
            dp[i] = min(dp[i], dp[i-3]+cost[2])

    # 12월까지 계산 결과 vs 1년권
    result = min(dp[12], cost[3])
    print(f'#{tc} {result}')