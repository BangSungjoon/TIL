# 버블 정렬
def bubble_sort(arr):
    for i in range(len(arr) -1):
        for j in range(len(arr) -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr
    
def bubble_sort2(arr):
    for i in range(len(arr) -1, 0, -1):

        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flg = True
        
        if not flg : return arr
    return arr