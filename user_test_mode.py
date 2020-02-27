# User testing mode contains code for user to test each function

from algorithms import gcd as gcd, fibonacci as fib, exponent as exp, sorting as sort

task_1_prompt_file = open('task_1_prompt.txt')
task_1_prompt = task_1_prompt_file.read()
print(task_1_prompt)
k = int(input())
print("Fib(", k, ") is:", fib.seq(k))
print("GCD(", k + 1, ",", k, ") is:", gcd.value(k + 1, k))
task_1_prompt_file.close()

print("\n")

task_2_prompt_file = open('task_2_prompt.txt')
task_2_prompt_part_2_file = open('task_2_prompt_part_2.txt')
task_2_prompt = task_2_prompt_file.read()
print(task_2_prompt)
a = int(input())
task_2_prompt_part_2 = task_2_prompt_part_2_file.read()
print(task_2_prompt_part_2)
n = int(input())
print("Decrease by One for [", a, ",", n, "] is: ", exp.dec_by_one(a, n))
print("Decrease by Constant Factor for [", a, ",", n, "] is: ", exp.dec_by_fctr(a, n))
print("Divide and Conquer for [", a, ",", n, "] is: ", exp.div_and_conq(a, n))
task_2_prompt_file.close()
task_2_prompt_part_2_file.close()

print("\n")

sort_task = open('task_3_prompt.txt')
sort_prompt = sort_task.read()
print(sort_prompt)
s_arr = list(map(int, input('Enter elements for list:\n').split()))
i_arr = s_arr.copy()
c1 = sort.select_sort(s_arr)
print('Selection Sort: ', s_arr, '\nComparisons: ', c1)
c2 = sort.insert_sort(i_arr)
print('Insertion Sort: ', i_arr, '\nComparisons: ', c2)



# x = 7
# print("7 + what = 10?")
# y = int(input())
# print(y)
# if y == 3:
#     print("correct!")
# else:
#     print("wrong :(")
