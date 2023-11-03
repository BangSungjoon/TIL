def partition(arr, low, high):
    pivot = arr[low]
    j = low
    for i in range(low + 1, high + 1):
        print(arr,low,j)
        if arr[i] < pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
        
    pivot = j
    arr[low], arr[pivot] = arr[pivot], arr[low]
    return pivot
    
def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot -1)
        quicksort(arr, pivot+1, high)
    
    return arr

# stack으로 구현한 quicksort
def quicksort_stack(arr):
    pass