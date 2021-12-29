# This problem involves Group Theory, Burnside's Theorem and Polya Enumeration Theory
# It essentially asks for the number of equivalence classes in an W x H matrix with S states
#
# Interchanging any 2 rows (or columns) of a matrix any number of times gives all possible permutations
# for an n row matrix this represent n! permutations
# The permutations of a row or column can be represented by the Symmetric Group
# so we need to take the direct product of two symmetric groups and then find the number of equivalence classes
# The Cycle Index of the Symmetric groups is found individually then direct product is calculated

# Function to generate the partitions of an integer
# the partitions correspond to all possible cycles in the permutations of the Symmetric Group Sn
def integerPartitions(n):
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
    while ip[0] > 1:  # check leftmost digit
        if ip[-1] > 1:  # check rightmost digit
            ip[-1] -= 1  # decrement rightmost digit
            addDigit(ip)  # add additional digits as needed
            yield ip
        else:
            ip.pop()  # when rightmost digit reaches 1, remove it from the list


# Function to calculate the coefficients in the Cycle Index using the cycle structure
def cycleIndexCoefficient(partition, n):

    # create dictionary to aggregate integers and count cycles of each length from 1 to n
    cycles = {}
    for i in partition:
        if i in cycles:
            cycles[i] += 1
        else:
            cycles[i] = 1

    # Calculate the Cycle Index coefficient using the cycle structure
    denom = 1
    for cycleLength, numCycles in cycles.items():
        denom *= cycleLength ** numCycles * fact(numCycles)
    return fact(n) / denom


# Function to calculate the greatest common denominator (gcd)
# Note that the least common multiple (LCM) can be calculated from the gcd
# LCM(a,b) = a*b / gcd(a,b)
# this function uses Euclid's method
def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a

# Function to calculate factorials
# The largest factorial needed in the problem is 12!= 479001600 , as W and H are limited to 12
def fact(n):
    for i in range(1,n):
        n *= i
    return n


# Main function - will calculate the number of equivalence classes in the direct product of 2 symmetric groups
def solution(w, h, s):

    # Initialize variable that will accumulate the terms for the calculated Direct Product Cycle Index polynomial
    dpci = 0
    # iterate over array of all W and H partition combinations
    for wPartition in integerPartitions(w):
        for hPartition in integerPartitions(h):
            # combine the Cycle Index coefficient of each W,H pair in the array
            cic = cycleIndexCoefficient(wPartition, w) * cycleIndexCoefficient(hPartition, h)
            gcdSum = 0
            # iterate over each cycle length in the current Cycle Index polynomial terms for the W and H partitions
            # combine each i,j combination using the gcd function 
            for j in hPartition:
                for i in wPartition:
                  gcdSum += gcd(i,j)
            # accumulate the terms of the Cycle Index of the Direct Product of the 2 symmetric groups
            # we have the coefficient times the # of states (similar to colourings in Group theory)
            # raised to an exponent. This parallels the terms on the Cycle Index polynomial of the individual
            # symmetric groups
            dpci += cic * (s**gcdSum)

    return str(dpci//(fact(w)*fact(h)))  # divide by w! x h! to account for all permutations of the direct product


if __name__ == "__main__":


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