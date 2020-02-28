# gcd function
def gcd(m, n, gcd_mod_arr, i):
    if n <= 1:
        return 1
    if m == 0:
        return n
    if n == 0:
        return m
    gcd_mod_arr[i] += 1
    return gcd(n, m % n, gcd_mod_arr, i)
