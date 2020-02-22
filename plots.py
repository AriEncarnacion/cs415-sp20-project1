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
