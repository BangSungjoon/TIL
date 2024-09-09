# 16690. 5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree
def pre_order(T):
    global cnt
    if T:
        cnt += 1
        pre_order(left[T])
        pre_order(right[T])

T = int(input())

for test_case in range(1, T+1):
    E, N = map(int, input().split())        # E는 간선의 개수, 서브 트리가 시작할 노드 N
    arr = list(map(int, input().split()))   # 입력 받은 배열

    left = [0]*(E+2)
    right = [0]*(E+2)
    cnt = 0

    for i in range(E):                      # left와 right에 채워넣기
        parent, child = arr[i*2], arr[i*2+1]

        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    pre_order(N)
    print(f'#{test_case} {cnt}')