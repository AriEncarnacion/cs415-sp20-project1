# fibonacci sequence functions


# addCount
#   counts the amount of additions to calculate F(n)
def addCount(fib_add_n):
    if fib_add_n <= 1:
        return 0
    return addCount(fib_add_n - 1) + addCount(fib_add_n - 2) + 1


# seq
#   calculate the fibonacci number returned from F(n)
def seq(fib_seq_n):
    if fib_seq_n == 0:
        return 0
    if fib_seq_n == 1:
        return 1
    return seq(fib_seq_n - 1) + seq(fib_seq_n - 2)
