# plotting functions

import matplotlib.pyplot as plt
import time
import gc


# fibAddsPlot
#   plots the number of additions from fibonacci.py/addCount
#   as n increases
def fib_adds_plot(fib_arr):
    plt.title('A(k) - Fibonacci Recursive Additions')
    plt.xlabel('k')
    plt.ylabel('Additions')
    plt.plot(fib_arr, label='add ops', color='red')
    plt.plot(fib_arr, 'r.')
    plt.legend()

    tm = time.gmtime()
    save_name = "Fibonacci_A_k " + time.strftime("%Y-%m-%d %H:%M:%S", tm)
    plt.savefig('generated_plots/' + save_name + '.png')

    plt.show()
    print("addArr:", fib_arr)

    gc.collect()


# gcdModsPlot
#   plots the number of modulo operations from gcd.py/modCount
#   as n increases
def gcd_mods_plot(gcdModsArr):
    plt.title('D(n) - GCD Worst Case Modulo Operations')
    plt.xlabel('n')
    plt.ylabel('Modulo Operations')
    plt.plot(gcdModsArr, label='mod ops.', color='blue')
    plt.plot(gcdModsArr, 'b.')
    plt.legend()

    tm = time.gmtime()
    save_name = "gcd_D_n " + time.strftime("%Y-%m-%d %H:%M:%S", tm)
    plt.savefig('generated_plots/' + save_name + '.png')

    plt.show()
    print("gcdModsArr:", gcdModsArr)

    gc.collect()


# expPlots
def exp_plots(dbo_arr, dbf_arr, dac_arr):
    dbo_plot(dbo_arr)
    dbf_plot(dbf_arr)
    dac_plot(dac_arr)

    plt.title('M(n) - Multiplications for 3 Exponent Algorithms')
    plt.xlabel('n')
    plt.ylabel('Multiplications')

    plt.plot(dbo_arr, label='Decrease by One', color='red')
    plt.plot(dbo_arr, 'r.')
    plt.plot(dbf_arr, label='Decrease by Constant Factor', color='blue')
    plt.plot(dbf_arr, 'b.')
    plt.plot(dac_arr, label='Divide and Conquer', color='green')
    plt.plot(dac_arr, 'g.')
    plt.legend()

    tm = time.gmtime()
    save_name = "Exponent_M_n " + time.strftime("%Y-%m-%d %H:%M:%S", tm)
    plt.savefig('generated_plots/' + save_name + '.png')

    plt.show()

    print("dec_by_one_plot:", dbo_arr)
    print("dec_by_fctr_plot:", dbf_arr)
    print("div_and_conq_plot:", dac_arr)

    gc.collect()


def dbo_plot(dbo_arr):
    plt.title("Decrease By One: D(n) - Multiplications")
    plt.xlabel('n')
    plt.ylabel('Multiplications')
    plt.plot(dbo_arr, label='Decrease By One', color='red')
    plt.plot(dbo_arr, 'r.')

    tm = time.gmtime()
    save_name = "dec_by_one_M_n " + time.strftime("%Y-%m-%d %H:%M:%S", tm)
    plt.savefig('generated_plots/' + save_name + '.png')
    plt.show()


def dbf_plot(dbf_arr):
    plt.title("Decrease By Constant Factor: D(n) - Multiplications")
    plt.xlabel('n')
    plt.ylabel('Multiplications')
    plt.plot(dbf_arr, label='Decrease by Constant Factor', color='blue')
    plt.plot(dbf_arr, 'b.')

    tm = time.gmtime()
    save_name = "dec_by_cons_factor_M_n " + time.strftime("%Y-%m-%d %H:%M:%S", tm)
    plt.savefig('generated_plots/' + save_name + '.png')
    plt.show()


def dac_plot(dac_arr):
    plt.title("Divide and Conquer: D(n) - Multiplications")
    plt.xlabel('n')
    plt.ylabel('Multiplications')
    plt.plot(dac_arr, label='Divide and Conquer', color='green')
    plt.plot(dac_arr, 'g.')

    tm = time.gmtime()
    save_name = "div_and_conq_M_n " + time.strftime("%Y-%m-%d %H:%M:%S", tm)
    plt.savefig('generated_plots/' + save_name + '.png')
    plt.show()


def select_sort_avg(arr):
    plt.title("Selection Sort Average-Case")
    plt.xlabel('n')
    plt.ylabel('C(n)')
    plt.plot(arr, label='comparisons', color='blue')
    plt.plot(arr, 'b.')
    plt.legend()

    tm = time.gmtime()
    save_name = "select_sort_avg" + time.strftime("%Y-%m-%d %H:%M:%S", tm)
    plt.savefig('generated_plots/' + save_name + '.png')

    plt.show()
    print("sel_avg n=", len(arr), ":", arr[len(arr)-1])

    gc.collect()


def select_sort_best(arr):
    plt.title("Selection Sort Best-Case")
    plt.xlabel('n')
    plt.ylabel('C(n)')
    plt.plot(arr, label='comparisons', color='green')
    plt.plot(arr, 'g.')
    plt.legend()

    tm = time.gmtime()
    save_name = "select_sort_best" + time.strftime("%Y-%m-%d %H:%M:%S", tm)
    plt.savefig('generated_plots/' + save_name + '.png')

    plt.show()
    print("sel_best, n=", len(arr), ":", arr[len(arr)-1])

    gc.collect()


def select_sort_worst(arr):
    plt.title("Selection Sort Worst-Case")
    plt.xlabel('n')
    plt.ylabel('C(n)')
    plt.plot(arr, label='comparisons', color='red')
    plt.plot(arr, 'r.')
    plt.legend()

    tm = time.gmtime()
    save_name = "select_sort_worst" + time.strftime("%Y-%m-%d %H:%M:%S", tm)
    plt.savefig('generated_plots/' + save_name + '.png')

    plt.show()
    print("sel_worst, n=", len(arr), ":", arr[len(arr)-1])

    gc.collect()


def insert_sort_avg(arr):
    plt.title("Insertion Sort Average-Case")
    plt.xlabel('n')
    plt.ylabel('C(n)')
    plt.plot(arr, label='comparisons', color='blue')
    plt.plot(arr, 'b.')
    plt.legend()

    tm = time.gmtime()
    save_name = "insertion_sort_avg" + time.strftime("%Y-%m-%d %H:%M:%S", tm)
    plt.savefig('generated_plots/' + save_name + '.png')

    plt.show()
    print("ins_avg, n=", len(arr), ":", arr[len(arr)-1])

    gc.collect()


def insert_sort_best(arr):
    plt.title("Insertion Sort Best-Case")
    plt.xlabel('n')
    plt.ylabel('C(n)')
    plt.plot(arr, label='comparisons', color='green')
    plt.plot(arr, 'g.')
    plt.legend()

    tm = time.gmtime()
    save_name = "insertion_sort_best" + time.strftime("%Y-%m-%d %H:%M:%S", tm)
    plt.savefig('generated_plots/' + save_name + '.png')

    plt.show()
    print("ins_best, n=", len(arr), ":", arr[len(arr)-1])

    gc.collect()


def insert_sort_worst(arr):
    plt.title("Insertion Sort Worst-Case")
    plt.xlabel('n')
    plt.ylabel('C(n)')
    plt.plot(arr, label='comparisons', color='red')
    plt.plot(arr, 'r.')
    plt.legend()

    tm = time.gmtime()
    save_name = "insertion_sort_worst" + time.strftime("%Y-%m-%d %H:%M:%S", tm)
    plt.savefig('generated_plots/' + save_name + '.png')

    plt.show()
    print("ins_worst, n=", len(arr), ":", arr[len(arr)-1])

    gc.collect()
