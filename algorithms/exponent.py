def dec_by_one(a, n, dbo_array, i):
    if a == 1:
        return 1
    if n == 0:
        return 1
    dbo_array[i] += 1
    return dec_by_one(a, n - 1, dbo_array, i) * a


def dec_by_fctr(a, n, dbf_array, i):
    if a == 1:
        return 1
    if n == 0:
        return 1
    if n % 2 == 0:
        dbf_array[i] += 1
        return dec_by_fctr(a, n / 2, dbf_array, i) ** 2
    dbf_array[i] += 2
    return a * dec_by_fctr(a, (n - 1) / 2, dbf_array, i) ** 2


def div_and_conq(a, n, dac_array, i):
    if a == 1:
        return 1
    if n == 0:
        return 1
    if n % 2 == 0:
        dac_array[i] += 1
        return div_and_conq(a, (n / 2), dac_array, i) * div_and_conq(a, (n / 2), dac_array, i)
    dac_array[i] += 2
    return a * div_and_conq(a, (n - 1) / 2, dac_array, i) * div_and_conq(a, (n - 1) / 2, dac_array, i)
