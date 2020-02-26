# Plotting mode file contains tests for each module
# fib.x runs fibonacci.py functions
# gcd.x runs gcd.py functions

from algorithms import gcd as gcd, fibonacci as fib, exponent as exp
import plots as plt

# arrays to hold basic operation count for current k-value
addArr = []
gcdModsArr = []
dboArr = []
dbfArr = []
dacArr = []

# calculate basic operations
n = 30
for k in range(0, n + 1):
    addArr.append(fib.add_count(k))

    gcdInput2 = fib.seq(k)
    gcdInput1 = fib.seq(k + 1)
    gcdModsArr.append(gcd.modCount(gcdInput1, gcdInput2))

    dboArr.append(exp.dbo_count(2, k))
    dbfArr.append(exp.dbf_count(2, k))
    dacArr.append(exp.dac_count(2, k))

# plot all basic operations
plt.fib_adds_plot(addArr)
plt.gcd_mods_plot(gcdModsArr)
plt.exp_plots(dboArr, dbfArr, dacArr)

