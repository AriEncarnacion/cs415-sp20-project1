# Main file contains tests for each module
# fib.x runs fibonacci.py functions
# gcd.x runs gcd.py functions

from algorithms import gcd as gcd, fibonacci as fib
import sorting as sort
import plots as plot
import random2


# addArr = []
# gcdModsArr = []

# for k in range(0, n + 1):
#     addArr.append(fib.addCount(k))
#     gcdInput2 = fib.seq(k)
#     gcdInput1 = fib.seq(k + 1)
#     gcdModsArr.append(gcd.modCount(gcdInput1, gcdInput2))
#
# plot.fibAddsPlot(addArr)
# plot.gcdModsPlot(gcdModsArr)

i_arr_Avg = []
i_arr_Best = []
i_arr_Worst = []
s_arr_Avg = []
s_arr_Best = []
s_arr_Worst = []
n = 30


rand_arr = []
sorted_arr = []
rev_arr = []

for k in range(n):
    for i in range(k):
        rand_arr.append(random2.randint(1, 50))

    s_arr_Avg.append(sort.count_s_sort(rand_arr))
    i_arr_Avg.append(sort.count_i_sort(rand_arr))
    rand_arr.clear()

    sorted_arr.append(k)
    rev_arr.append(n - k)
    s_arr_Best.append(sort.count_s_sort(sorted_arr))
    s_arr_Worst.append(sort.count_s_sort(rev_arr))

    i_arr_Best.append(sort.count_i_sort(sorted_arr))
    i_arr_Worst.append(sort.count_i_sort(rev_arr))

plot.s_sort_plot(s_arr_Avg)
plot.s_sort_plot(s_arr_Best)
plot.s_sort_plot(s_arr_Worst)

plot.i_sort_plot(i_arr_Avg)
plot.i_sort_plot(i_arr_Best)
plot.i_sort_plot(i_arr_Worst)
