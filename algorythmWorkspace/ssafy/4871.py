# 16493. 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로
def dfs(start, goal):
    global way
    visited[start] = 1
    if start == goal:
        way = 1
        return
    else:
        for a in adj_l[start]:
            if visited[a] == 0:
                dfs(a, goal)

T = int(input())

for test_case in range(1, T+1):
    # V는 노드의 개수, E는 간선의 개수
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    way = 0
    visited = [0]*(V+1)
    visited[S] = 1

    # 인접 리스트 만들기, 방향은 단방향
    adj_l = [[] for _ in range(V+1)]
    for i in range(E):
        adj_l[arr[i][0]].append(arr[i][1])

    dfs(S, G)

    print(f'#{test_case} {way}')
