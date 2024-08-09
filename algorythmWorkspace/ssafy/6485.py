# 삼성시의 버스 노선
T = int(input())

for test_case in range(1, T+1):
    N = int(input())    # 버스노선 개수
    road = [list(map(int, input().split())) for _ in range(N)]  # 버스노선 2차원 배열로 입력 받기
    P = int(input())    # 정류장 개수
    station = [int(input()) for _ in range(P)]  # 정류장 번호 입력 받기
    result = [0]*P      # 출력할 결과 배열 만들기

    for i in range(N):  # 버스노선 수 만큼 검사해야하니 N만큼 순회
        for j in range(P):  # 각 정류장이 노선의 범위안에 있다면
            if station[j] in range(road[i][0], road[i][1]+1):
                result[j] += 1  # 해당 정류장에 다니는 버스 노선의 수 1증가

    print(f'#{test_case}', *result)