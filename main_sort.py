from algorithms import sorting as sort
import plots as plot
import random2

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

for k in range(0, n):
    for i in range(k):
        rand_arr.append(random2.randint(1, 50))

    rand_arr2 = rand_arr.copy()
    s_arr_Avg.append(sort.count_s_sort(rand_arr))
    i_arr_Avg.append(sort.count_i_sort(rand_arr2))
    rand_arr.clear()

    sorted_arr.append(k)
    rev_arr = sorted_arr.copy()
    rev_arr.reverse()
    print("sorted:", sorted_arr)
    print("reversed:", rev_arr)
    rev_arr2 = rev_arr.copy()
    s_arr_Best.append(sort.count_s_sort(sorted_arr))
    s_arr_Worst.append(sort.count_s_sort(rev_arr))

    i_arr_Best.append(sort.count_i_sort(sorted_arr))
    i_arr_Worst.append(sort.count_i_sort(rev_arr2))


plot.select_sort_avg(s_arr_Avg)
plot.select_sort_best(s_arr_Best)
plot.select_sort_worst(s_arr_Worst)

plot.insert_sort_avg(i_arr_Avg)
plot.insert_sort_best(i_arr_Best)
plot.insert_sort_worst(i_arr_Worst)