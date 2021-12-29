def solution(n):
    from math import sqrt, floor
    from decimal import *
    n = long(n)

    getcontext().prec = 200

    sr2 = Decimal(2)**Decimal(0.5)

    np = long(floor((sr2 - 1) * n))
    npd = ((sr2 - 1) * n)//1
    print np, npd
    ss1 = n*np + n*(n+1)/2 - np*(np+1)/2

    # print n, 'ss1 =', ss1, np

    sign = 1

    while np > 0:
        n = np
        np = long(floor((sr2 - 1) * n))
        ss = (n*np + n*(n+1)/2 - np*(np+1)/2)
        ss1 -= ss * sign
        # print ss1, " -> ", n, 'ss =', ss, np, sign
        sign = - sign

    return str(long(ss1))

def sol(n):
    from math import sqrt, floor

    n = int(n)
    i = 1
    s = 0

    while i < n + 1:
        yield int(floor(i * sqrt(2)))
        # s += floor(i*sqrt(2))
        # yield int(s)
        i+=1

def sol2(n):
    n = long(s)

    def terms(n):
        from math import floor, sqrt

        i = 1

        while i < n + 1:
            yield int(floor(i * sqrt(2)))
            i += 1

    return str(sum(terms(n)))



# for i in range(10):
#     print solution(i+1)
#     print sum([j for j in sol(i+1)])
#
# print solution(77)
# print sum([i for i in sol(77)])
#
# for i in range(100,5000,100):
#     print solution(i+1)
#     print sum([j for j in sol(i + 1)])

print solution(5)
print solution(770000000000000000)