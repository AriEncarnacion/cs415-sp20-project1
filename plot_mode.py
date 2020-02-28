# Plotting mode file contains tests for each module
# fib.x runs fibonacci.py functions
# gcd.x runs gcd.py functions

from algorithms import gcd as gcd, fibonacci as fib, exponent as exp, sorting as sort
import plots as plt
import random2

# calculate basic operations
# A(k) -- Count of Fibonacci recursive additions
print("## Running A(k) ##")
fib_count_arr = []
for k in range(0, 26):
    fib_count_arr.append(0)
    fib.fib(k, fib_count_arr, k)
print("A(k) complete")

# D(n) -- Count of Euclid modulus operations for the GCD
# Will calculate  50 iterations
print("\n## Running D(n) ##")
print("iteratively building fibonacci sequnece array for D(n)")
iterations = 51  # iterations will become 50 due to range() function
fib_seq_literal = [0, 1]
for n in range(2, 51):
    fib_seq_literal.append(fib_seq_literal[n - 1] + fib_seq_literal[n - 2])

gcd_mods_arr = []
for n in range(0, 50):
    gcd_mods_arr.append(0)
    a = fib_seq_literal[n + 1]
    b = fib_seq_literal[n]
    gcd.gcd(a, b, gcd_mods_arr, n)
print("D(n) complete")

# M(n) -- Count of multiplications for three different
# implementations of exponentiation
print("\n## Running M(n) ##")
dbo_arr, dbf_arr, dac_arr = [], [], []
for n in range(0, 51):
    dbo_arr.append(0)
    dbf_arr.append(0)
    dac_arr.append(0)
    exp.dec_by_one(2, n, dbo_arr, n)
    exp.dec_by_fctr(2, n, dbf_arr, n)
    exp.div_and_conq(2, n, dac_arr, n)
print("M(n) complete")

print("\n## Plotting all arithmetic algorithms ##")
# plot all basic operations
print("plotting A(k)")
plt.fib_adds_plot(fib_count_arr)
print("plotting D(n)")
plt.gcd_mods_plot(gcd_mods_arr)
print("plotting M(n)")
plt.exp_plots(dbo_arr, dbf_arr, dac_arr)

print("\n## Running sorting ##")
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

print("\n## Plotting all sorting algorithms ##")
# Plots for each C(n) list
print("plotting selection sort (average)")
plt.select_sort_avg(s_a)
print("plotting selection sort (best)")
plt.select_sort_best(s_b)
print("plotting selection sort (worst)")
plt.select_sort_worst(s_w)

print("plotting insertion sort (average)")
plt.insert_sort_avg(i_a)
print("plotting insertion sort (best)")
plt.insert_sort_best(i_b)
print("plotting insertion sort (worst)")
plt.insert_sort_worst(i_w)

print("\nAll tasks complete.\n")

