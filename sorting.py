# Selection Sort
def select_sort(arr):
    n = len(arr)
    i = 0
    while i < n:
        k = i
        j = i + 1
        while j < n:
            if arr[j] < arr[k]:
                k = j
            j += 1
        t = arr[i]
        arr[i] = arr[k]
        arr[k] = t
        i += 1


# Insertion Sort
def insert_sort(arr):
    n = len(arr)
    i = 1
    while i < n:
        k = i
        while k > 0 and arr[k] < arr[k-1]:
            t = arr[k]
            arr[k] = arr[k-1]
            arr[k-1] = t
            k -= 1
        i += 1


# Main

s_arr = [9, 3, 7, 45, 98, 2, 65, 7, 13, 48]
print(s_arr)
insert_sort(s_arr)
#select_sort(s_arr)
print(s_arr)
