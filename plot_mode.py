# Plotting mode file contains tests for each module
# fib.x runs fibonacci.py functions
# gcd.x runs gcd.py functions

from algorithms import gcd as gcd, fibonacci as fib, exponent as exp, sorting as sort
import plots as plt
import random2

# calculate basic operations
# A(k) -- Count of Fibonacci recursive additions
fib_count_arr = []
for k in range(0, 26):
    fib_count_arr.append(0)
    fib.fib(k, fib_count_arr, k, "plot")

# D(n) -- Count of Euclid modulus operations for the GCD
# Will calculate  50 iterations
iterations = 51  # iterations will become 50 due to range() function
fib_seq_literal = [0, 1]
for n in range(2, 51):
    fib_seq_literal.append(fib_seq_literal[n - 1] + fib_seq_literal[n - 2])

print("Fibonacci sequence literal", fib_seq_literal)

gcd_mods_arr = []
for n in range(0, 50):
    gcd_mods_arr.append(0)
    a = fib_seq_literal[n + 1]
    b = fib_seq_literal[n]
    gcd.gcd(a, b, gcd_mods_arr, n, "plot")

# M(n) -- Count of multiplications for three different
# implementations of exponentiation
dbo_arr, dbf_arr, dac_arr = [], [], []
for n in range(0, 51):
    dbo_arr.append(0)
    dbf_arr.append(0)
    dac_arr.append(0)
    exp.dec_by_one(2, n, dbo_arr, n, "plot")
    exp.dec_by_fctr(2, n, dbf_arr, n, "plot")
    exp.div_and_conq(2, n, dac_arr, n, "plot")

# plot all basic operations
plt.fib_adds_plot(fib_count_arr)
plt.gcd_mods_plot(gcd_mods_arr)
plt.exp_plots(dbo_arr, dbf_arr, dac_arr)

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
