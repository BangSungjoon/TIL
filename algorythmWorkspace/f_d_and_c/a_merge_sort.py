from d_queue import Queue

# [1,5,7,13] [2,4,9,12,15]

def merge(arr1, arr2):
    res = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    if i < len(arr1):
        res += arr1[i:len(arr1)]
    else:
        res += arr2[j:len(arr2)]

    return res

# 재귀함수로 구현한 merge sort
def mergesort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        mid = n // 2
        arr1 = mergesort(arr[0:mid])
        arr2 = mergesort(arr[mid:n])
        return merge(arr1,arr2)

# queue
def mergesort2(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    queue = Queue()
    for e in arr:
        queue.enqueue([e])

    while len(queue) > 1:
        arr1 = queue.dequeue()
        arr2 = queue.dequeue()
        queue.enqueue(merge(arr1,arr2))
    
    return queue.dequeue()