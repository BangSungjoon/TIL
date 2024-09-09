# 1232. [S/W 문제해결 기본] 9일차 - 사칙연산
def cal(node):
    if node:                            # node의 값이 0이 아니라면
        left = cal(left_child[node])    # 왼쪽 자식
        right = cal(right_child[node])  # 오른쪽 자식
        if tree[node] == '+':
            tree[node] = left + right
        elif tree[node] == '-':
            tree[node] = left - right
        elif tree[node] == '/':
            tree[node] = left // right
        elif tree[node] == '*':
            tree[node] = left * right
    return tree[node]                   # 연산을 해야하니 반환해줍시다 인간적으로

for test_case in range(1, 11):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]

    tree = [0]*(N+1)
    left_child = [0]*(N+1)
    right_child = [0]*(N+1)

    # tree에 값 넣어 주기
    for i in range(N):
        if arr[i][1] in '+-*/':     # 기호라면 int로 변환하지 않고 저장
            tree[int(arr[i][0])] = arr[i][1]
        else:                       # 기호가 아니라면(숫자) int로 변환 후 저장
            tree[int(arr[i][0])] = int(arr[i][1])
        if len(arr[i]) == 4:        # 만약 자식이 있는 노드라면
            left_child[int(arr[i][0])] = int(arr[i][2])     # 왼쪽 자식 배열
            right_child[int(arr[i][0])] = int(arr[i][3])    # 오른쪽 자식 배열
    print(f'#{test_case} {cal(1)}')                         # 최종 연산 값 등장