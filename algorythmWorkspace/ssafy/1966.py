# 숫자를 정렬하자

# bubble sort
def bubble(arr, n):
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# counting sort
def counting_sort(arr, n):
    counting_arr = [0]*(11)
    # 1. counting_arr에 arr내 원소의 빈도 수 담기
    for a in arr:
        counting_arr[a] += 1
    # 2. 누적 counting_arr으로 업데이트
    for i in range(1, len(counting_arr)):
        counting_arr[i] += counting_arr[i-1]
    # 3. 정렬된 결과를 담을 result 초기화
    result = [0]*len(arr)
    # 4. 뒤부터 정렬하기
    for i in range(len(arr)-1, -1, -1):
        counting_arr[arr[i]] -= 1
        result[counting_arr[arr[i]]] = arr[i]

    return result

# selection sort
def select(arr, n):
    for i in range(0, n):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    result = select(numbers, N)
    print(f'#{test_case}', end=' ')
    for k in result:
        print(k, end=' ')
    print()