# Main file contains tests for each module
# fib.x runs fibonacci.py functions
# gcd.x runs gcd.py functions

import fibonacci as fib
import gcd as gcd
import plots as plot


addArr = []
gcdModsArr = []
n = 30
for k in range(0, n + 1):
    addArr.append(fib.addCount(k))
    gcdInput2 = fib.seq(k)
    gcdInput1 = fib.seq(k + 1)
    gcdModsArr.append(gcd.modCount(gcdInput1, gcdInput2))

plot.fibAddsPlot(addArr)
plot.gcdModsPlot(gcdModsArr)
