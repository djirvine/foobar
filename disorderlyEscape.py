# from math import fact
# from collections import Counter
# from fractions import gcd

def cycle_count(pl, n):
    d = {}
    for e in pl:
        if e in d:
            d[e] += 1
        else:
            d[e] = 1

    denom = 1
    for cycle, numCycles in d.items():
        denom *= cycle ** numCycles * fact(numCycles)
    return fact(n) / denom

def cycle_partitions(n):
    # 1st run
    ip = [n]
    yield ip

    # function to add digit to the list
    # added digit cannot be greater than the last digit in the list
    def addDigit(ip):
        last = ip[-1]
        ni = n - sum(ip)
        if ni > last:
            ni = last
            ip += [ni]
            addDigit(ip)
        else:
            ip += [ni]
        return ip

    # generate list of partitions by continuously decrementing last element of list
    # when last element reaches 1, then remove it and repeat
    # stop when first element of list equals 1
    # this is the case of n ones
    while ip[0] > 1:
        if ip[-1] > 1:
            ip[-1] -= 1
            addDigit(ip)
            yield ip
        else:
            ip.pop()


def GCD(a,b):
    return a if b == 0 else GCD(b,a%b)

def GCD2(a,b):
    while b != 0:
        # t = b
        # b = a%b
        # a = t

        # r = a % b
        # a,b = b,r

        a, b = b, a%b

    return a

def fact(n):
    for i in range(1,n):
        n *= i
    return n

def solution(w, h, s):
    matrixSum=0
    for cpw in cycle_partitions(w):
        for cph in cycle_partitions(h):
            # print "cpw",cpw,"cph",cph
            m=cycle_count(cpw, w)*cycle_count(cph, h)
            # print "ccw", cycle_count(cpw, w), "cch",cycle_count(cph, h),"m",m
            # grid+=m*(s**sum([sum([gcd(i, j) for i in cpw]) for j in cph]))
            sum=0
            for j in cph:
                for i in cpw:
                  sum+= GCD2(i,j)
            # print "gcd sum = ", sum
            matrixSum += m * (s**sum)
            # print "matrixSum =", matrixSum
            # for x in cpw: print "cpw(x)",x
    print "ANSWER = ", matrixSum//(fact(w)*fact(h)),"\n"
    return str(matrixSum//(fact(w)*fact(h)))

print "********", GCD(1071,462), GCD2(1071,462)

print "**************"
solution(2,2,2)  # 7
print solution(2,3,4)  # 430
print solution(2,3,2)  # 13
print solution(12,12,20)  # 97195340925396730736950973830781340249131679073592360856141700148734207997877978005419735822878768821088343977969209139721682171487959967012286474628978470487193051591840
print solution(3,5,20)  # 45568090499534008
print solution(4,4,20)  # 1137863754106723400
print solution(5,5,20)  # 23301834615661488487765745000
print solution(6,6,20)  # 132560781153101038829213988789736592649360
print solution(7,7,20)  # 221619886894198821201872678876163305792210161226545392840
print solution(8,8,20)  # 113469378614817897312718329989374518983724697432844009920312263602471667640

print solution(3, 3, 3)  # 738
print solution(3, 3, 4)  # 8240
print solution(3, 3, 5)  # 57675
print solution(4, 4, 4)  # 7880456
print solution(4, 4, 5)  # 270656150
print solution(5, 5, 5)  # 20834113243925