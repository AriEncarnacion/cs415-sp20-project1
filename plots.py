# plotting functions

import matplotlib.pyplot as plt
import time

# fibAddsPlot
#   plots the number of additions from fibonacci.py/addCount
#   as n increases
def fib_adds_plot(addArr):
    plt.title('Fibonacci Additions')
    plt.xlabel('n')
    plt.ylabel('Basic Operations')
    plt.plot(addArr, label='add ops', color='red')
    plt.plot(addArr, 'r.')
    plt.legend()

    plt.show()
    print("addArr:", addArr)


# gcdModsPlot
#   plots the number of modulo operations from gcd.py/modCount
#   as n increases
def gcd_mods_plot(gcdModsArr):
    plt.title('GCD Worst Case')
    plt.xlabel('n')
    plt.ylabel('Basic Operations')
    plt.plot(gcdModsArr, label='mod ops.', color='blue')
    plt.plot(gcdModsArr, 'b.')
    plt.legend()

    plt.show()
    print("gcdModsArr:", gcdModsArr)


# expPlots
def exp_plots(dbo_arr, dbf_arr, dac_arr):
    plt.title('Exponentiation')
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
    save_name = "Exponent_M_n " + time.strftime("%Y-%m-%d %H:%M:%S", tm) + ".png"
    # print(save_name)
    plt.savefig('generated_plots/save')

    plt.show()
    print("dec_by_one_plot:", dbo_arr)
    print("dec_by_fctr_plot:", dbf_arr)
    print("div_and_conq_plot:", dac_arr)