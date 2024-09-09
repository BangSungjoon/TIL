# 16711. 5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙
def enq(num):           # 최소 이진 힙 입력 함수
    global last
    last += 1           # 마지막 노드 1 증가
    tree[last] = num    # 마지막 노드에 입력받은 숫자 넣기
    child = last
    parent = child//2

    # 부모가 있고, 부모가 더 크다면
    while parent >= 1 and tree[parent] > tree[child]:
        tree[parent], tree[child] = tree[child], tree[parent]   # 자리 바꾸기
        child = parent
        parent = child // 2

T = int(input())

for test_case in range(1, T+1):
    N = int(input())    # 노드의 수
    arr = list(map(int, input().split()))

    tree = [0]*(N+1)    # 인덱스 1번부터 넣어줄거니깐 한 칸 더
    last = 0
    final = N//2        # 마지막 노드의 부모 노드 번호
    result = 0          # 조상들을 더할 결과 값

    for i in arr:       # 배열을 돌며 최소 이진 힙 입력하기
        enq(i)
    # 이진 힙이 완성됐다면 마지막 노드의 조상들을 더해주기
    while final >= 1:
        result += tree[final]
        final //= 2

    print(f'#{test_case} {result}')