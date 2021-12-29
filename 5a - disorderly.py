from math import factorial
from collections import Counter
from fractions import gcd

def cycle_count(c, n):
    cc=factorial(n)
    for a, b in Counter(c).items():
        # print "a", a,"b", b
        # print Counter(c)
        cc//=(a**b)*factorial(b)
    print "cc", cc
    return cc

def cycle_partitions(n, i=1):
    # print "n", n
    yield [n]
    # print "n",n, "n//2+1", n//2+1
    # print "i*", i
    for i in range(i, n//2+1):
        # print "i",i
        for p in cycle_partitions(n-i, i):
            # print "i",i,"p",p
            yield [i]+p

def solution(w, h, s):
    grid=0
    for cpw in cycle_partitions(w):
        for cph in cycle_partitions(h):
            print "cpw",cpw,"cph",cph
            m=cycle_count(cpw, w)*cycle_count(cph, h)
            grid+=m*(s**sum([sum([gcd(i, j) for i in cpw]) for j in cph]))
            for x in cpw: print "cpw(x)",x
    return grid//(factorial(w)*factorial(h))


for cp in cycle_partitions(7):
    print "cp", cp

def y(n):
    yield [n]
    for i in range(n-1, 0, -1):
        yield [i]+[n]

# for e in y(5):
#     print e

print "**************"
# print solution(2,2,2)  # 7
print solution(2,3,4)  # 430
# print solution(2,3,2)  # 13
# print solution(12,12,20)  # 97195340925396730736950973830781340249131679073592360856141700148734207997877978005419735822878768821088343977969209139721682171487959967012286474628978470487193051591840
# print solution(3,5,20)  # 45568090499534008
# print solution(4,4,20)  # 1137863754106723400
# print solution(5,5,20)  # 23301834615661488487765745000
# print solution(6,6,20)  # 132560781153101038829213988789736592649360
# print solution(7,7,20)  # 221619886894198821201872678876163305792210161226545392840
# print solution(8,8,20)  # 113469378614817897312718329989374518983724697432844009920312263602471667640
#
# print solution(3, 3, 3)  # 738
# print solution(3, 3, 4)  # 8240
# print solution(3, 3, 5)  # 57675
# print solution(4, 4, 4)  # 7880456
# print solution(4, 4, 5)  # 270656150
# print solution(5, 5, 5)  # 20834113243925
