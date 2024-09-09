# 16689. 5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색
def inorder(node, n, arr, result):
    if node <= n:   # 현재 노드가 노드의 최대값보다 작거나 같다면
        inorder(node*2, n, arr, result)     # 왼쪽 자식노드 값 넣기
        result[node] = arr.pop(0)           # 현재 노드에 값 넣기
        inorder(node*2+1, n, arr, result)   # 오른쪽 자식노드 값 넣기

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    # 들어가야 할 값들, 1부터 N까지의 자연수
    arr = list(range(1, N+1))
    result = [0]*(N+1)      # 완전 이진 트리 형태인 이진 탐색 트리

    # 중위탐색에 값을 전달
    inorder(1, N, arr, result)

    root = result[1]
    div_node = result[N//2]

    print(f'#{test_case} {root} {div_node}')