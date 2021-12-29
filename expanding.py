def solution(g):

    # print matrix
    def pm(m):

        for r in range(len(m)):
            print m[r]
        print

    for r in range(len(g)):
        for c in range(len(g[0])):
            g[r][c] = g[r][c] * 1

    pm(g)

    prev = [[None] * (len(g[0])+1) for i in range(len(g)+1)]
    pm(prev)

    def ckp1(r,c):
        print "checking previous around 1 at", r, c
        
        if ckPone(r,c-1):
            return True
        elif ckPone(r+1,c-1):
            return True
        elif ckPone(r+1,c):
            return True
        else:
            return False

    def ckPone(r,c):
        print "testing at", r, c
        if prev[r][c] == 1:
            prev[r][c] = 0
            print "set to zero"
            return False
        elif prev[r][c] == 1:
            print "error - is one"
            return True
        else:
            print "already zero"
            return False


    def ckzero(r,c):
        print "checking around 0 at", r, c

        if ckZ(r,c+1):
            return True
        elif ckZ(r+1,c):
            return True
        elif ckZ(r+1,c+1):
            return True
        else:
            return False

    def ckZ(r,c):
        print "testing at",r,c
        if prev[r][c] == None:
            prev[r][c] = 0
            print "set to zero"
            return False
        elif prev[r][c] == 1:
            print "error - is one"
            return True
        else:
            print "already zero"
            return False


    def ckone(r,c):
        print "checking around 1 at", r, c

        if ckZN(r,c+1):
            return True
        elif ckZN(r+1,c):
            return True
        elif ckZN(r+1,c+1):
            return True
        else:
            return False

    def ckZN(r,c):
        print "testing at",r,c
        if prev[r][c] == None:
            prev[r][c] = 0
            print "set to zero"
            return False
        elif prev[r][c] == 1:
            print "error - is one"
            return True
        else:
            print "already zero"
            return False


    # def check(r,c):
    #     print r,c
    #     if r < len(prev)-1 and c < len(prev[0])-1:
    #         if g[r][c] == 1:
    #             if c > 0:
    #                 if prev[r][c]+prev[r+1][c] == 0:
    #                     prev[r][c+1]=1
    #                     prev[r+1][c+1]=0
    #                 else:
    #                     prev[r][c + 1] = 0
    #                     prev[r + 1][c + 1] = 0
    #             else:
    #
    #                 prev[r][c] = 1
    #                 prev[r][c + 1] = 0
    #                 prev[r + 1][c] = 0
    #                 prev[r + 1][c + 1] = 0
    #         else:
    #             if (prev[r][c] + prev[r + 1][c]) == 0:
    #                 prev[r][c+1] = 0
    #             else:
    #                 prev[r][c+1] = 1
    #
    #
    #     if g[r][c] == 0:
    #         if None in [prev[r][c + 1], prev[r + 1][c] , prev[r + 1][c + 1]]:
    #             prev[r][c]=0
    #         else:
    #             if (prev[r][c + 1] + prev[r + 1][c] + prev[r + 1][c + 1]) == 0:
    #                 prev[r][c]=0
    #             else:
    #                 prev[r][c] = 1

    loop = True

    # start at top left
    r = 0
    c = 0

    while loop:
        print "working on cell at",r,c
        #1st col
        # update cell value if empty
        if prev[r][c] == None:

            if c == 0:
                prev[r][c] = 1
            else:
                if g[r,c] == 1:
                    ckp1(r,c)
                else:
                    ckp0(r,c)

            pm(prev)
            # zero out surroundings if current state=1
            if r < len(prev)-2:
                if g[r][c] == 1:
                    if ckone(r,c):
                        print "Error"
                        break


        if prev[r][c] ==0:
            if r < len(prev)-2:
                if g[r][c] == 0:
                    if ckzero(r,c):
                        print "Error"
                        break


        # check(r,c)
        pm(prev)
        # increment row
        r=r+1

        # reached end of row, go to next column
        if r > len(prev)-1:
            r=0
            c=c+1
            if c > len(prev[0])-1:
                # reached the end, stop looping
                loop = False
    pm(prev)
    pm(g)

    # for cell in [1, 0]:
    #     # either all True(c[0][0] and 1 cell) or all False (!c[0][0] and !1 cell)
    #     if (not a or not b) or len(set([((past[a][b-1] + past[a-1][b]
    #         + past[a-1][b-1] + cell)==1), state[a-1][b-1]]))==1:
    #             history.append(cell)
    #             past[a][b] = cell
    #             res+=answer(state, a=(a+1)%(len(state)+1),
    #                     b=b+(a+1)//(len(state)+1), past=past,
    #                     solutions=solutions, history=history)
    #             history.pop()




g = [[True, False, True], [False, True, False], [True, False, True]]

solution(g)