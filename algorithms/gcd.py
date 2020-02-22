# gcd functions

# gcd
#   calculates the number of modulo operations in gcd(m,n)
def modCount(gcd_m, gcd_n):
    if gcd_n <= 1:
        return 0
    return modCount(gcd_n, gcd_m % gcd_n) + 1
