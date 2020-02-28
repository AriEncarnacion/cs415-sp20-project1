def dec_by_one(a, n, dbo_array, i, mode):
    if n == 0:
        return 1
    if mode == "plot":
        dbo_array[i] += 1
    return dec_by_one(a, n - 1, dbo_array, i, mode) * a


def dec_by_fctr(a, n, dbf_array, i, mode):
    if n == 0:
        return 1
    if n % 2 == 0:
        if mode == "plot":
            dbf_array[i] += 1
        return dec_by_fctr(a, n / 2, dbf_array, i, mode) ** 2
    if mode == "plot":
        dbf_array[i] += 1
    return a * dec_by_fctr(a, (n - 1) / 2, dbf_array, i, mode) ** 2


def div_and_conq(a, n, dac_array, i, mode):
    if n == 0:
        return 1
    if n % 2 == 0:
        if mode == "plot":
            dac_array[i] += 1
        return div_and_conq(a, (n / 2), dac_array, i, mode) * div_and_conq(a, (n / 2), dac_array, i, mode)
    if mode == "plot":
        dac_array[i] += 2
    return a * div_and_conq(a, (n - 1) / 2, dac_array, i, mode) * div_and_conq(a, (n - 1) / 2, dac_array, i, mode)
