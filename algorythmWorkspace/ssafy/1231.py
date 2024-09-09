# 1231. [S/W 문제해결 기본] 9일차 - 중위순회
def inorder(node, n, tree):         # 중위순회
    global result
    if node <= n:                   # 범위를 벗어나지 않았다면
        inorder(node*2, n, tree)    # 왼쪽 탐색
        result += tree[node]        # 탐색이 끝났다면 추가욧
        inorder(node*2+1, n, tree)  # 오른쪽 탐색

for test_case in range(1, 11):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    tree = [0]*(N+1)                        # 트리 노드별 들어갈 값 리스트
    result = ''                             # 정답이 될 문자열

    # Tree에 값 넣기
    for i in range(N):
        tree[int(arr[i][0])] = arr[i][1]

    inorder(1, N, tree)                     # 1번부터 N번까지

    print(f'#{test_case} {result}')