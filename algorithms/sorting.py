import random2
import plots as plot


# Selection Sort Params
# arr:  list - unsorted
# returns comparisons c
def select_sort(arr):
    i, c = 0, 0
    while i < len(arr)-1:
        k = i
        j = i + 1
        while j < len(arr):
            c += 1
            if arr[j] < arr[k]:
                k = j
            j += 1
        arr[i], arr[k] = arr[k], arr[i]
        i += 1
    return c


# Insertion Sort Params
# arr:  list - unsorted
# returns comparisons c
def insert_sort(arr):
    i, c = 1, 0
    while i < len(arr):
        k = i
        while k > 0 and arr[k] < arr[k-1]:
            c += 1
            arr[k], arr[k-1] = arr[k-1], arr[k]
            k -= 1
        if k != 0:
            c += 1
        i += 1
    return c

