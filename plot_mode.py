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
# A(k) -- Count of Fibonacci recursive additions
for k in range(0, 26):
    addArr.append(fib.add_count(k))

# D(n) -- Count of Euclid modulus operations for the GCD
fib_seq_literal = [0, 1]
for n in range(2, 51):
    fib_seq_literal.append(fib_seq_literal[n - 1] + fib_seq_literal[n - 2])

print("Fibonacci sequence literal", fib_seq_literal)

for n in range(0, 50):
    a = fib_seq_literal[n + 1]
    b = fib_seq_literal[n]
    print("a:", a, "b:", b)
    gcdModsArr.append(gcd.modCount(a, b))

# M(n) -- Count of multiplications for three different
# implementations of exponentiation
for n in range(0, 51):
    dboArr.append(exp.dbo_count(2, n))
    dbfArr.append(exp.dbf_count(2, n))
    dacArr.append(exp.dac_count(2, n))

# plot all basic operations
plt.fib_adds_plot(addArr)
plt.gcd_mods_plot(gcdModsArr)
plt.exp_plots(dboArr, dbfArr, dacArr)
