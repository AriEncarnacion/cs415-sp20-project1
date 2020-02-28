# User testing mode contains code for user to test each function

from algorithms import gcd as gcd, fibonacci as fib, exponent as exp, sorting as sort


responses = ['y', 'Y', 'n', 'N']
response = 'y'
while response == 'y' or response == 'Y':
    fib_arr, gcd_arr = [0], [0]

    task_1_prompt_file = open('task_1_prompt.txt')
    task_1_prompt = task_1_prompt_file.read()

    print(task_1_prompt)

    k = int(input("Enter a value for 'k' (recommended k < 36):"))

    print("Fib(", k, ") is:", fib.fib(k, fib_arr, 0))
    print("Additions:", fib_arr[0])
    print("GCD(", k + 1, ",", k, ") is:", gcd.gcd(k + 1, k, gcd_arr, 0))
    print("Modulos:", gcd_arr[0])

    task_1_prompt_file.close()

    response = input("Would you like to repeat this task? y/n: ")
    while response not in responses:
        print("Please enter 'y' to repeat or 'n' to continue to the next task.")
        response = input("Would you like to repeat this task? y/n: ")
    print("\n")


response = 'y'
while response == 'y' or response == 'Y':
    dbo_arr, dbf_arr, dac_arr = [0], [0], [0]
    task_2_prompt_file = open('task_2_prompt.txt')
    task_2_prompt = task_2_prompt_file.read()

    print(task_2_prompt)

    a = int(input("Enter a value for 'a':"))
    n = int(input("Enter a value for 'n':"))

    print("Decrease by One for [", a, ",", n, "] is: ", exp.dec_by_one(a, n, dbo_arr, 0))
    print("Multiplications:", dbo_arr[0])
    print("Decrease by Constant Factor for [", a, ",", n, "] is: ", exp.dec_by_fctr(a, n, dbf_arr, 0))
    print("Multiplications:", dbf_arr[0])
    print("Divide and Conquer for [", a, ",", n, "] is: ", exp.div_and_conq(a, n, dac_arr, 0))
    print("Multiplications:", dac_arr[0])

    task_2_prompt_file.close()

    response = input("Would you like to repeat this task? y/n: ")
    while response not in responses:
        print("Please enter 'y' to repeat or 'n' to continue to the next task.")
        response = input("Would you like to repeat this task? y/n: ")
    print("\n")


response = 'y'
while response == 'y' or response == 'Y':
    sort_task = open('task_3_prompt.txt')
    sort_prompt = sort_task.read()
    print(sort_prompt)
    s_arr = list(map(int, input('Enter elements for list:\n').split()))
    i_arr = s_arr.copy()
    c1 = sort.select_sort(s_arr)
    print('Selection Sort: ', s_arr, '\nComparisons: ', c1)
    c2 = sort.insert_sort(i_arr)
    print('Insertion Sort: ', i_arr, '\nComparisons: ', c2)

    response = input("Would you like to repeat this task? y/n: ")
    while response not in responses:
        print("Please enter 'y' to repeat or 'n' to continue to the next task.")
        response = input("Would you like to repeat this task? y/n: ")

print("\nAll tasks complete.")
