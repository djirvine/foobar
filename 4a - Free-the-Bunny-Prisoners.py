from copy import deepcopy

def solution(num_buns, num_required):

    # if (num_req - 1) buns is not a solution then when you pick a random set of (num_req - 1) buns
    # all of the remaining buns (i.e. [num_buns - (num_req -1)] must have a unique key that the (num_req - 1) buns do
    # not have.
    # we therefore need to find the number of combinations for picking [num_buns - (num_req -1)] from num_buns
    # to determine how many keys we need to hand out
    # a unique key goes to each set of [num_buns - (num_req -1)] and each set requires [num_buns - (num_req -1)] copies
    # of the key

    sets =  num_buns - (num_required - 1)

    # generate empty key list for all the buns
    kl = []
    for b in range(num_buns):
        kl.append([])


    # use enumerate to count all of the combos found, which is also the number of the keys
    for k, bl in enumerate(combo(num_buns, sets)):
        # print k, bl
        for b in bl:
            kl[b].append(k)

    # print kl
    return kl


# function to create a list of all of the unique combinations C(n,r)
# the number of combinations is given by C(n, r) = n! / r! / (n-r)!
def combo(n, r):

    def cycle(n,r, pos):

        # check for digit to the right
        # print "current pos = ", pos
        if pos < r-1:
            # check if it is maxed out
            if c[pos + 1] < n - (r - (pos + 1)):
                cycle(n, r, pos+1)

            # else maxed out to the right
            else:
                # increment current digit if not maxed out
                if c[pos] < n - (r - pos):
                    c[pos] += 1
                    # reset all digits to the right
                    left = c[pos]
                    for i in range(pos+1, r):
                        c[i] = left + 1
                        left += 1
                    # print "reset to the right", pos +1
                    # print c
                    cl.append(deepcopy(c))
                    # print cl
                    cycle(n, r, pos + 1)

                # else if current digit maxed out, move left if it exists
                else:
                    if pos - 1 >= 0:
                        cycle(n, r, pos -1)

                    # else nothing to the left so end
                    else:
                        return

        # nothing to the right, so check if current digit is maxed out
        if c[pos] < n - (r - pos):
            c[pos] += 1
            # print c
            cl.append(deepcopy(c))
            # print cl
            cycle(n, r, pos)

        # nothing to the right, but maxed out, so increment to the left
        else:
            # check if something exists to the left
            if pos >= 0:
                cycle(n,r, pos - 1)

            # nothing to the left
            else:
                return

    # build initial list for first combo
    c=[]
    pos = 0
    for i in range(r):
        c.append(i)
        pos = i

    # blank list to hold all combos found
    cl = []

    # print c
    cl.append(deepcopy(c))
    # print cl

    # call cycle to run through all of the combos available
    cycle(n, r, pos)
    return cl


# test cases
for n,r in [(3,1), (2,2), (3,2), (2,1), (4,4), (5,3)]:
    s = solution(n,r)
    print "\n"
    print s


