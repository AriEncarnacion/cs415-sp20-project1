# fibonacci sequence
def fib(n, fib_add_arr, i, mode):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if mode == "plot":
        fib_add_arr[i] += 1
    return fib(n - 1, fib_add_arr, i, mode) + fib(n - 2, fib_add_arr, i, mode)
