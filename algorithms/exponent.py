import math


def dec_by_one(a, n):
    if n == 0:
        return 1
    return dec_by_one(a, n - 1) * a


def dbo_count(a, n):
    if n == 0:
        return 0
    return dbo_count(a, n - 1) + 1


def dec_by_fctr(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return dec_by_fctr(a, n / 2) ** 2
    return a * dec_by_fctr(a, (n - 1) / 2) ** 2


def dbf_count(a, n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return dbf_count(a, n / 2) + 1
    return dbf_count(a, (n - 1) / 2) + 1


def div_and_conq(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return div_and_conq(a, (n / 2)) * div_and_conq(a, (n / 2))
    return a * div_and_conq(a, (n - 1) / 2) * div_and_conq(a, (n - 1) / 2)


def dac_count(a, n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return dac_count(a, (n / 2)) + 1
    return dac_count(a, (n - 1) / 2) + 2
