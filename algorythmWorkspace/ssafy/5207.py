# 18797. 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색
def binary_search(low, high, target, vector):
    global cnt
    # 기저 조건
    # target을 찾지 못했다면 종료
    if low > high:
        return

    mid = (low + high) // 2

    # 발견했고 왕복 두 번 이상 했다면
    if target == n_arr[mid]:
        cnt += 1
        return
    elif target < n_arr[mid]:
        if vector == 'first' or vector == 'right':
            return binary_search(low, mid-1, target, 'left')
        else:   # 갔던 방향으로 또 갔으면 넌 자격이 없다
            return  # 돌아갓~!
    else:
        if vector == 'first' or vector == 'left':
            return binary_search(mid+1, high, target, 'right')
        else:
            return



T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())    # N: n_arr의 길이, M: m_arr의 길이
    n_arr = list(map(int, input().split()))
    m_arr = list(map(int, input().split()))
    cnt = 0

    n_arr = sorted(n_arr)    # 서로 다른 정수 N개가 주어지면 정렬한 상태로 n_arr에 저장

    # m_arr에 저장된 M개의 정수에 대해 n_arr에 들어이는 수인지 이진 탐색으로 확인
    for i in range(M):
        binary_search(0, N-1, m_arr[i], 'first')

    print(f'#{test_case} {cnt}')