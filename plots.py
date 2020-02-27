# plotting functions

import matplotlib.pyplot as plt
import time

# fibAddsPlot
#   plots the number of additions from fibonacci.py/addCount
#   as n increases
def fib_adds_plot(addArr):
    plt.title('A(k) - Fibonacci Recursive Additions')
    plt.xlabel('n')
    plt.ylabel('Additions')
    plt.plot(addArr, label='add ops', color='red')
    plt.plot(addArr, 'r.')
    plt.legend()

    tm = time.gmtime()
    save_name = "Fibonacci_A_k " + time.strftime("%Y-%m-%d %H:%M:%S", tm)
    plt.savefig('generated_plots/' + save_name + '.png')

    plt.show()
    print("addArr:", addArr)


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


# expPlots
def exp_plots(dbo_arr, dbf_arr, dac_arr):
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


def select_sort_avg(arr):
    plt.title("Select Avg")
    plt.xlabel('n')
    plt.ylabel('C(n)')
    plt.plot(arr, label='comparisons', color='red')
    plt.plot(arr, 'bo')
    plt.legend()
    plt.show()
    print("sel_avg:", arr)


def select_sort_best(arr):
    plt.title("Select Best")
    plt.xlabel('n')
    plt.ylabel('C(n)')
    plt.plot(arr, label='comparisons', color='red')
    plt.plot(arr, 'bo')
    plt.legend()
    plt.show()
    print("sel_best:", arr)


def select_sort_worst(arr):
    plt.title("Select Worst")
    plt.xlabel('n')
    plt.ylabel('C(n)')
    plt.plot(arr, label='comparisons', color='red')
    plt.plot(arr, 'bo')
    plt.legend()
    plt.show()
    print("sel_worst:", arr)


def insert_sort_avg(arr):
    plt.title("Insertion Sort Avg")
    plt.xlabel('n')
    plt.ylabel('C(n)')
    plt.plot(arr, label='comparisons', color='red')
    plt.plot(arr, 'bo')
    plt.legend()
    plt.show()
    print("ins_avg:", arr)


def insert_sort_best(arr):
    plt.title("Insertion Sort Best")
    plt.xlabel('n')
    plt.ylabel('C(n)')
    plt.plot(arr, label='comparisons', color='red')
    plt.plot(arr, 'bo')
    plt.legend()
    plt.show()
    print("ins_best:", arr)


def insert_sort_worst(arr):
    plt.title("Insertion Sort Worst")
    plt.xlabel('n')
    plt.ylabel('C(n)')
    plt.plot(arr, label='comparisons', color='red')
    plt.plot(arr, 'bo')
    plt.legend()
    plt.show()
    print("ins_worst:", arr)