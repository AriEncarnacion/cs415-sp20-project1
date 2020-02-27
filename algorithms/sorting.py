import random2
import plots as plot

# Selection Sort
def select_sort(arr):
    n = len(arr)
    c = 0
    i = 0
    while i < n-1:
        k = i
        j = i + 1
        while j < n:
            c += 1
            if arr[j] < arr[k]:
                k = j
            j += 1
        t = arr[i]
        arr[i] = arr[k]
        arr[k] = t
        i += 1
    return c

# Insertion Sort
def insert_sort(arr):
    n = len(arr)
    c = 0
    i = 1
    while i < n:
        k = i
        c += 1
        while k > 0 and arr[k] < arr[k-1]:
            c += 1
            t = arr[k]
            arr[k] = arr[k-1]
            arr[k-1] = t
            k -= 1
        i += 1
    return c


def count_s_sort(arr):
    return select_sort(arr)


def count_i_sort(arr):
    return insert_sort(arr)
