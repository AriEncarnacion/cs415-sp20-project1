# fibonacci sequence
def fib(n, fib_add_arr, i):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib_add_arr[i] += 1
    return fib(n - 1, fib_add_arr, i) + fib(n - 2, fib_add_arr, i)
