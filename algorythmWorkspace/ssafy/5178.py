# 22053. 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합
def back_order(node, N, li):
    if node <= N:
        left = back_order(node*2, N, li)    # 왼쪽 자식
        right = back_order(node*2+1, N, li) # 오른쪽 자식
        li[node] += left + right            # 현재 노드에 왼쪽 자식과 오른쪽 자식값 더해주기
        return li[node]                     # left + right 더하는 연산을 하므로 return 값이 있어야 한다.
    else:                                   # 범위를 벗어났다면
        return 0                            # 0 반환

T = int(input())

for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    arr = [list(map(int, input().split())) for _ in range(M)]

    # 순회 돌면서 tree의 리프 노드에 입력 받은 값 넣어주기
    for i in range(M):
        tree[arr[i][0]] = arr[i][1]

    back_order(1, N, tree)

    print(f'#{test_case} {tree[L]}')