from math import factorial
from integerPart import intPart

def cycleCount(pl,n):
    denom = 1
    for cycle, numCycles in pl.items():
        denom *= cycle**numCycles * factorial(numCycles)
    return factorial(n) / denom

# summarize partition list using a dictionary
def sumPL(pl):
    d = {}
    for e in pl:
        if e in d:
            d[e] += 1
        else:
            d[e] = 1
    return d

for e in intPart(5):

    pl = sumPL(e)
    print pl

    print cycleCount(pl, 5)