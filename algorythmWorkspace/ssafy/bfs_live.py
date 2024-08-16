import sys

sys.stdin = open('input.txt')

"""
라이브 강의 진행 코드 (인접 리스트)
"""


def bfs(s, V):  # 시작정점 s, 마지막 정점 V
    visited = [0] * (V + 1)  # visited 생성
    q = []  # 큐 생성
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시
    while q:  # 큐에 정점이 남아있으면 front != rear
        t = q.pop(0)  # 디큐
        print(t)  # 방문한 정점에서 할일
        for w in adj_l[t]:  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w] == 0:
                q.append(w)  # w인큐, 인큐되었음을 표시
                visited[w] = visited[t] + 1


V, E = map(int, input().split())  # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
# 인접리스트 -------------------------
adj_l = [[] for _ in range(V + 1)]
for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)  # 방향이 없는 경우
# 여기까지 인접리스트 -----------------
bfs(1, 7)

####################################################################################

"""
라이브 강의 진행 코드 (인접행렬)
"""
# def bfs(s, V):  # 시작정점 s, 마지막 정점 V
#     visited = [0] * (V + 1)  # visited 생성
#     q = []  # 큐 생성
#     q.append(s)  # 시작점 인큐
#     visited[s] = 1  # 시작점 방문표시
#     while q:  # 큐가 비어있지 않은 동안 반복
#         t = q.pop(0)  # 디큐
#         print(t)  # 방문한 정점 출력
#         for w in range(1, V + 1):  # 모든 노드에 대해
#             # 현재 노드와 연결되어 있고, 아직 방문하지 않은 노드라면
#             if adj_m[t][w] == 1 and visited[w] == 0:
#                 q.append(w)  # w 인큐, 인큐 되었음을 표시
#                 visited[w] = visited[t] + 1
#     # print(visited)


# V, E = map(int, input().split())  # 1번부터 V번 정점, E개의 간선
# arr = list(map(int, input().split()))  # 간성 정보

# # 인접행렬
# adj_m = [[0] * (V + 1) for _ in range(V + 1)]

# for i in range(E):
#     v1, v2 = arr[i * 2], arr[i * 2 + 1]
#     adj_m[v1][v2] = 1
#     adj_m[v2][v1] = 1  # 방향이 없는 경우

# bfs(1, V)
