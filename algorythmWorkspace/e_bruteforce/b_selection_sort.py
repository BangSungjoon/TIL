def selection_sort(arr):
    for p in range(len(arr) -1):
        min = p

        for i in range(p, len(arr)):
            if arr[min] > arr[i]:
                min = i

        arr[p], arr[min] = arr[min], arr[p]

    return arr