# plotting functions

import matplotlib.pyplot as plt

# fibAddsPlot
#   plots the number of additions from fibonacci.py/addCount
#   as n increases
def fibAddsPlot(addArr):
    plt.title('Fibonacci Additions')
    plt.xlabel('n')
    plt.ylabel('Basic Operations')
    plt.plot(addArr, label='add ops', color='red')
    plt.plot(addArr, 'ro')
    plt.legend()
    plt.show()
    print("addArr:", addArr)


# gcdModsPlot
#   plots the number of modulo operations from gcd.py/modCount
#   as n increases
def gcdModsPlot(gcdModsArr):
    plt.title('GCD Worst Case')
    plt.xlabel('n')
    plt.ylabel('Basic Operations')
    plt.plot(gcdModsArr, label='mod ops.', color='blue')
    plt.plot(gcdModsArr, 'bo')
    plt.legend()
    plt.show()
    print("gcdModsArr:", gcdModsArr)


def s_sort_plot(s_arr):
    plt.title('Selection Sort Average Case')
    plt.xlabel('n')
    plt.ylabel('C(n)')
    plt.plot(s_arr, label='comparisons', color='red')
    plt.plot(s_arr, 'bo')
    plt.legend()
    plt.show()
    print("select_sort:", s_arr)


def i_sort_plot(i_arr):
    plt.title('Insertion Sort Average Case')
    plt.xlabel('n')
    plt.ylabel('C(n)')
    plt.plot(i_arr, label='comparisons', color='green')
    plt.plot(i_arr, 'bo')
    plt.legend()
    plt.show()
    print("insertion_sort:", i_arr)
