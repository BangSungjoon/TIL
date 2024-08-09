# DFS 재귀

import  sys
from pprint import pprint

sys.stdin = open('input.txt')

# 정점의 개수, 간선의 개수
V, E = map(int, input().split())

# 간선 정보
data = list(map(int, input().split()))
print(data)  # [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# 인접행렬 생성
# 빈 도화지 만들기
matrix = [[0] * (V+1) for _ in range(V+1)]

for i in range(E):
    n1 = data[i*2]
    n2 = data[i*2+1]
    matrix[n1][n2] = 1
    matrix[n2][n1] = 1

visited = [0] * (V + 1)     # 방문 여부를 체크하는 리스트

def DFS(start):
    # 방문 기록
    visited[start] = 1
    # 방문한 노드를 출력
    print(start, end=' ')

    # 다음으로 조사가 가능한 노드 찾기
    for next in range(1, V+1):
        # 현재 노드에 인접해있고, 방문한 적이 없는 곳
        if matrix[start][next] == 1 and visited[next] == 0:
            # 또다시 탐색 시작
            DFS(next)

DFS(1)


'''
DFS 재귀함수의 종료 조건
- 암묵적인 종료 조건
    - 현재 노드에서 더 이상 방문할 수 있는 인접 노드가 없을 때 함수 종료
    - for 반복에서 모든 노드를 검사 했지만 조건을 만족하는 노드가 없다면 종료
'''

'''
동작 과정
1. DFS(1) 호출
2. 1번 노드 방문 표시 및 출력
3. 1번 노드의 인접 노드 중 방문하지 않은 2번 노드 발견
4. DFS(2)
5. 2번 노드 방문 표시 및 출력
6. 2번 노드의 인접 노드 중 방문하지 않은 4번 노드 발견
7. DFS(4)
8. ...
9. 마지막 노드에서 더 이상 방문할 인접 노드가 없음
10. 이전 호출로 돌아가며 남은 인접 노드 확인
11. 모든 노드 방문 완료 시 전체 DFS가 종료료
'''