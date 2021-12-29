import math

# best and simplest solution
def sol1(n):
    n = int(n)

    count = 0

    while n > 1:

        if n % 2 != 0:

            if (n) & 3 == 3 and n != 3:  # avoid 3's
                n += 1

            else:
                n -= 1

        else:
            n /= 2

        count += 1

    return count



def sol2(n):
    n = int(n)
    res = 0

    while (n != 1):
        if (n % 2 == 0):
            n = n / 2
        elif ((n == 3) or ((n + 1) & n) > ((n - 1) & (n - 2))):
            n -= 1
        else:
            n += 1
        res += 1
    return res

def solution(n):

    n = int(n)

    # print "best = {0}".format(round(math.log(n,2)))

    count = 0

    op = ""
    # print "count = {0:4}, {1:4} = {1:8b} op = {2}".format(count, n, op)
    while n > 1:

        if n % 2 != 0:
            # print n, (n+1) & n, (n - 1) & (n - 2)
            if (n) & 3 == 3 and  n != 3: # avoid 3's
            # if (n + 1) & n == 0 and n != 3:  # test for all bits rolling over, also eliminate 3 as it is a special case

                n += 1
                op = "+"

            else:
                n -= 1
                op = "-"

        else:
            n /= 2
            op="/"
        count += 1

        # print "count = {0:4}, {1:4} = {1:8b} op = {2}".format(count, n, op)
        if n == 1:
            break

    return count

for i in range (1,46564):
    s = str(i)
    s1 = solution(s)
    s2 = sol2(s)

    if s1 != s2:
        print s, s1, s2
        break
    print i


# print solution("4")
# print solution("15")
# print solution("14")
# print solution("17")
# print solution("63")
# print solution("31")
# print solution("178")
