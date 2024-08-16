# 16651. 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리
T = int(input())

for test_case in range(1, T+1):
    # V: 노드 개수, E: 간선 개수
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    # S: 시작 노드, G: 도착 노드
    S, G = map(int, input().split())
    result = 0  # 결과

    adj_l = [[] for _ in range(V+1)]    # 인접 리스트
    for i in range(E):
        n1 = arr[i][0]
        n2 = arr[i][1]
        adj_l[n1].append(n2)
        adj_l[n2].append(n1)

    # Queue와 visited 준비
    visited = [0]*(V+1)
    q = [S]
    visited[S] = 1
    # 탐색
    while q:
        t = q.pop(0)
        for w in adj_l[t]:
            if w == G:
                result = visited[t]  # 결과는 지나온 간선 수
                q = []  # q를 비워주고
                break
            if visited[w] == 0:
                visited[w] = visited[t] + 1
                q.append(w)
    print(f'#{test_case} {result}')