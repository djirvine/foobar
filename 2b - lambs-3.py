def solution(lambs):

    hg = 0
    pg = 0

    while pg < lambs:
        pg += 2**hg
        if pg > lambs:
            break
        hg += 1


    f1 = 1
    f2 = 1
    hs = 2
    ps = f1 + f2

    while ps < lambs:
        f2, f1 = f1, f1 + f2
        ps += f1
        if ps > lambs:
            break
        hs += 1

    return hs - hg

for test in [8, 10, 143, 2048, 2**20, 10**9]:
    print(test, solution(test))