# 18796. 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬
def hoare_partition(left, right):
    # 기준점(pivot)이 위치해야 할 index를 구하는 함수
    pivot = A[left]
    i = left + 1
    j = right

    while i <= j:
        while i <= j and A[i] <= pivot:     # pivot보다 작은 놈들 pass (오른쪽으로)
            i += 1                          # 더 크다면 정지 (index 기록)
        while i <= j and A[j] >= pivot:     # pivot보다 큰 놈들 pass (왼쪽으로)
            j -= 1                          # 더 작다면 정지 (index 기록)
        if i < j:                           # j가 i보다 더 오른쪽에 있다면
            A[i], A[j] = A[j], A[i]         # 자리 바꾸기

    A[left], A[j] = A[j], A[left]         # 기준점이었던 pivot과
    # pivot보다 작은 수 중 가장 오른쪽에 있는 값을 바꿔준다. -> pivot 자리 확정
    return j    # 확정된 pivot index


def quick_sort(left, right):
    if left < right:    # 왼쪽보다 오른쪽이 더 크다면
        pivot = hoare_partition(left, right)    # 기준이 될 index인 pivot 구하기
        quick_sort(left, pivot-1)
        quick_sort(pivot+1, right)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    quick_sort(0, N-1)
    print(f'#{test_case} {A[N // 2]}')
