# 7465. 창용 마을 무리의 개수
def dfs(T):
    visited[T] = 1           # 현재 노드 방문 처리

    for v in adj_l[T]:
        if visited[v] == 0:  # 방문하지 않은 인접 리스트가 있다면
            dfs(v)           # 즉시 dfs

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    people = [list(map(int, input().split())) for _ in range(M)]
    visited = [0]*(N+1)
    adj_l = [[] for _ in range(N+1)]
    cnt = 0

    # 인접리스트 만들기, 단방향 그래프
    for i in range(M):
        if len(people[i]) == 2:
            adj_l[people[i][0]].append(people[i][1])
            adj_l[people[i][1]].append(people[i][0])

    # 모든 방문하지 않은 정점에서 dfs 실행
    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)
            cnt += 1    # dfs가 끝나면 무리가 하나 끝난거임

    print(f'#{test_case} {cnt}')
