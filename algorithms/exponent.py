def decByOne(a, n):
    if n == 0:
        return 1
    return decByOne(a, n - 1) * a

def dboCount(a, n):
    if n == 0:
        return 0
    return dboCount(a, n - 1) +1


def decByFctr(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        result = decByFctr(a, n/2)
        return result * result
    result2 = decByFctr(a, (n-1) / 2)
    return result2 * result2


def dbfCount(a, n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return dbfCount(a, n/2) + 1
    return dbfCount(a, (n-1) / 2) + 1


def divAndConq(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return divAndConq(a, (n/2)) * divAndConq(a, (n/2))
    return a * divAndConq(a, (n - 1)/2) * divAndConq(a, (n - 1)/2)


def dacCount(a, n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return dacCount(a, (n/2)) + 1
    return dacCount(a, (n - 1)/2) + 2
