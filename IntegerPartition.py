def intPart(n):
    l = n

    yield [n]

    ip = [n]+[0]

    for i in range(n):
        for j in range(n-1,0, -1):
            ip[i] = j

            ni = n - ip[i]

            ip[i+1]=ni
            yield ip

    # m = n - 1
    # ni = n - m
    # ip = [m, ni]
    # count = 0
    # while ni > 0:
    #
    #     # for i in range(m,0,-1):
    #     # print "i",i
    #     # ni = n - m
    #     # ip = [m, ni]
    #     print ip
    #     if ni > 1:
    #         ip[-1] -= 1
    #         ni = 1
    #         ip += [ni]
    #     # intPart(i)
    #     else:
    #         m -= 1
    #         ni = n - m
    #         if ni > m:
    #
    #             ni = n - 2 * m
    #             ip = [m, m, ni]
    #             # print ip, "==="
    #         else:
    #             ip = [m, ni]
    #
    #     count +=1
    #     if count > 7:
    #         break


def intP(n,m):
    ip = [n]
    print ip, "ip"
    yield ip


    for k in range (n-1, 0, -1):

        for j in intP(n-1,1):
            print "***", ip, ip[-1]
            if (n - ip[-1]) >= 0:
                yield [k] + j
            # print j
            # # m = n-1
            # ip = [j]
            # for i in range(j, 0, -1):
            #     if n - j - i > 1:
            #         intP(j, 1)
            #         yield ip + [i]



for e in intPart(5):
    print "yielded", e