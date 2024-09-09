# 18798. 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬
def merge_sort(arr):
    # 분할하여 정렬하는 함수
    if len(arr) == 1:     # 리스트의 길이가 1이라면 이미 정렬된 상태
        return arr

    mid = len(arr) // 2   # 리스트를 절반으로 나눌 인덱스
    left = arr[:mid]      # 리스트의 앞쪽 절반
    right = arr[mid:]     # 리스트의 뒤쪽 절반

    left = merge_sort(left)  # 재귀로 분할 및 정렬
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    # 왼쪽, 오른쪽 비교하며 정렬한 뒤 병합하는 함수
    result = [0]*(len(left) + len(right))   # 정렬하여 병합할 리스트 초기화
    l = r = 0   # l: left의 index, r: right의 index

    global cnt  # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 크다면
    if left[-1] > right[-1]:
        cnt += 1

    while l < len(left) and r < len(right): # 범위가 넘지 않는다면 반복
        if left[l] < right[r]:      # 왼쪽이 오른쪽 보다 작다면
            result[l+r] = left[l]   # 현재 칸에 왼쪽을 넣어주자
            l += 1                  # left의 인덱스 1 증가
        else:                       # 왼쪽이 오른쪽 보다 크다면
            result[l+r] = right[r]
            r += 1

    # 남은것 넣어주기 left나 right 둘 중 하나는 다 들어갔으니
    # while문 중 하나만 실행될 것이다.
    while l < len(left):
        result[l+r] = left[l]
        l += 1
    while r < len(right):
        result[l+r] = right[r]
        r += 1
    return result

T = int(input())

for test_case in range(1, T+1):
    N = int(input())                             # 정수의 개수
    number = list(map(int, input().split()))     # 입력받은 숫자열
    cnt = 0     # 정답이 될 병합 과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수

    answer = merge_sort(number)
    print(f'#{test_case} {answer[N//2]} {cnt}')