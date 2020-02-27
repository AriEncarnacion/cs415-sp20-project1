# Plotting mode file contains tests for each module
# fib.x runs fibonacci.py functions
# gcd.x runs gcd.py functions

from algorithms import gcd as gcd, fibonacci as fib, exponent as exp, sorting as sort
import plots as plt
import random2

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


### Sorting Plots ###
# i = insertion sort, s = selection sort
# a = average, b = best, w = worst

i_a, i_b, i_w = [], [], []
s_a, s_b, s_w = [], [], []

rand_arr = []
sorted_arr = []
rev_arr = []

for k in range(1, 101):

# Build list of random ints
    for i in range(k):
        rand_arr.append(random2.randint(1, 1000))

    rand_arr2 = rand_arr.copy()
    sorted_arr.append(k)
    rev_arr = sorted_arr.copy()
    rev_arr.reverse()
    rev_arr2 = rev_arr.copy()

# C(n) lists for all n and relative cases
    s_a.append(sort.select_sort(rand_arr))
    s_b.append(sort.select_sort(sorted_arr))
    s_w.append(sort.select_sort(rev_arr))

    i_a.append(sort.insert_sort(rand_arr2))
    i_b.append(sort.insert_sort(sorted_arr))
    i_w.append(sort.insert_sort(rev_arr2))

    rand_arr.clear()
    rand_arr2.clear()

# Plots for each C(n) list
plt.select_sort_avg(s_a)
plt.select_sort_best(s_b)
plt.select_sort_worst(s_w)

plt.insert_sort_avg(i_a)
plt.insert_sort_best(i_b)
plt.insert_sort_worst(i_w)
