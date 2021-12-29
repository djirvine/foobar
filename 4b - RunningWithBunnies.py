import copy

class V():
    def __init__(self):
        self.d = float("inf")
        self.p = None


class G():
    def __init__(self, AM):
        self.AM = AM
        self.numV = len(AM)
        self.V = [V() for i in range(self.numV)]  # vertices in graph
        self.lwp = [[[] for col in range(self.numV)] for row in range(self.numV)]  # initialize lowest weight path (lwp) matrix
        self.bulkhead = self.numV - 1
        self.longestPath = []

    # function for printing matrix nicely
    @classmethod
    def printAdjMatrix(cls, AM):
        for row in AM:
            print(row)
        print

    @classmethod
    def Initialize(cls, G, s):
        for v in G.V:
            v.d = float("inf")
            v.p = None
        G.V[s].d = 0

        return 0

    @classmethod
    def Relax(cls, u, v, G):

        # print(f"G.V[v].d = {G.V[v].d}, G.V[u].d = {G.V[u].d}")
        if True:
        # if G.AM[u][v] != 0:  # removed as zero time is still a valid edge weight
            # print(f"u={u}, v={v}")
            if G.V[v].d > G.V[u].d + G.AM[u][v]:
                G.V[v].d = G.V[u].d + G.AM[u][v]
                G.V[v].p = u

        # print(f"G.V[v].d = {G.V[v].d}, G.V[u].d = {G.V[u].d}")
        return 0

    @classmethod
    def BellmanFord(cls, G, s):

        G.Initialize(G, s)
        # for i, v in enumerate(G.V):
            # print(f"V[{i}].d = {v.d}")

        for i in range(len(G.AM)-1):
            for u, row in enumerate(G.AM):
                # print(f"\nrelaxing #{i}")
                for v, col in enumerate(row):
                    if u != v:
                        G.Relax(u, v, G)
                # print(f"\nafter relax #{i}")
        # print"BellmanFord"
        # G.printAdjMatrix(G.lwp)
        # check for negative cycle paths
        for u, row in enumerate(G.AM):
            for v, col in enumerate(row):
                if G.V[v].d > G.V[u].d + G.AM[u][v]:
                    # print "negative cycle", u, v, G.V[v].d,"<>", G.V[u].d, G.AM[u][v]
                    # print "start =", s

                    # G.printAdjMatrix(G.AM)
                    return False

        return True
    @classmethod
    def buildPath(cls, G, current, timeRemaining, path, count, done):
        if not done:

            # path = copy.deepcopy(path)
            # pathroot = copy.deepcopy(path)
            count += 1
            ##print "current=", current, "path=", path, "count=", count

            # numV = len(times)
            # try all vertices from current vertex except self
            for nextVertex in set(range(G.numV)) - {current}:
                # print "reseting path to ->", pathroot, path
                # path = pathroot
                # check if possible to get back to the bulk head after with time >=0 after moving to nextVertex
                if timeRemaining - G.lwp[current][nextVertex] - G.lwp[nextVertex][G.bulkhead] >= 0:
                    # feasible so add to path
                    # path.append(nextVertex)
                    ##print "found option"
                    ##print current,"->", nextVertex,"t-start=", timeRemaining, ",", "t-end=",timeRemaining - G.lwp[current][nextVertex], "+ t-bk =", timeRemaining - G.lwp[current][nextVertex]-G.lwp[nextVertex][G.bulkhead], path
                    if count > 7:
                        break
                    # timeRemaining -= G.lwp[current][nextVertex]
                    # print "calling"
                    G.buildPath(G, nextVertex, timeRemaining - G.lwp[current][nextVertex], path+[nextVertex], count, done)
                    # print "returned, path now=",path
                    # path.pop()
                # else:
                #     print " no option for", current, nextVertex, path
            ##print "final path found =", path
            currentLongestPath = set(path) - set([0, G.bulkhead])
            if len(currentLongestPath) > len(G.longestPath):
                G.longestPath = currentLongestPath
                ##print "\nBunnies picked up so far = ", G.longestPath,"\n"

            if len(G.longestPath) == G.numV-2:
                done = True
                ##print "Done, picked up all the bunnies!"

            return G.longestPath

        else:
            return G.longestPath


def solution(times, time_limit):
    G.printAdjMatrix(times)

    numV = len(times)

    # trivial case, no bunnies
    if numV == 2:
        print "No bunnies to pickup"
        bunniesPickedUp = []
        print "************\nBunnies Picked Up = ", bunniesPickedUp, "\n************\n\n"

        return bunniesPickedUp

    # initialize lowest weight path (lwp) matrix
    # lwp = [[[] for col in range(numV)] for row in range(numV)]

    g = G(times)

    # use BellmanFord to convert times matrix into a lowest weighted path (lwp) matrix
    for i, row in enumerate(g.lwp):
        # call BellmanFord for each possible starting point, to generate eah row of lwp matrix
        if not G.BellmanFord(g, i):
            # negative cycle present, therefore have infinite time and can collect all bunnies
            print "Negative cycle -> infinite time!!! Can pick up all the bunnies"
            bunniesPickedUp = list(range(numV - 2))
            print "************\nBunnies Picked Up = ", bunniesPickedUp, "\n************\n\n"

            return bunniesPickedUp
            # return list(range(numV - 2))
        for j, col in enumerate(g.lwp):
            g.lwp[i][j] = g.V[j].d
    G.printAdjMatrix(g.lwp)

    # Brute force iteration through all valid paths, saving longest path along the way

    bulkhead = numV - 1
    current = 0
    path = [current]

    timeRemaining = time_limit

    path = G.buildPath(g, current, timeRemaining, path, 0, False)

    path = list(path)

    bunniesPickedUp = []

    for v in path:
        bunniesPickedUp.append(v-1)

    print "************\nBunnies Picked Up = ", bunniesPickedUp,"\n************\n\n"

    return bunniesPickedUp







if __name__ == "__main__":

    times = [
    [0, 2, 2, 2, -1],  # 0 = Start
    [9, 0, 2, 2, -1],  # 1 = Bunny 0
    [9, 3, 0, 2, -1],  # 2 = Bunny 1
    [9, 3, 2, 0, -1],  # 3 = Bunny 2
    [9, 3, 2, 2,  0],  # 4 = Bulkhead
    ]

    ## G.printAdjMatrix(times)

    # numV = len(times)
    # lwp = [[[] for col in range(numV)] for row in range(numV)]
    #
    # printAdjMatrix(lwp)
    # print lwp

    assert solution(times, 1) == [1,2]

    times = [[0, 1, 5, 5, 2],
          [10, 0, 2, 6, 10],
          [10, 10, 0, 1, 5],
          [10, 10, 10, 0, 1],
          [10, 10, 10, 10, 0]] #5, [0, 1, 2])

    assert solution(times, 5) == [0, 1, 2]


    times = [[0, 1, 3, 4, 2],
          [10, 0, 2, 3, 4],
          [10, 10, 0, 1, 2],
          [10, 10, 10, 0, 1],
          [10, 10, 10, 10, 0]] #, 4, [])

    assert solution(times, 4)== []

    times = [[0, 1, 10, 10, 10],
          [10, 0, 1, 1, 2],
          [10, 1, 0, 10, 10],
          [10, 1, 10, 0, 10],
          [10, 10, 10, 10, 0]] #, 7, [0, 1, 2])

    assert solution(times, 7)== [0, 1, 2]


    times = [[0, 1, 1, 1, 1],
          [1, 0, 1, 1, 1],
          [1, 1, 0, 1, 1],
          [1, 1, 1, 0, 1],
          [1, 1, 1, 1, 0]] #, 3, [0, 1])

    assert solution(times,3)== [0, 1]

    times =[[0, 5, 11, 11, 1],
          [10, 0, 1, 5, 1],
          [10, 1, 0, 4, 0],
          [10, 1, 5, 0, 1],
          [10, 10, 10, 10, 0]] #, 10, [0, 1])

    solution(times, 10)

    assert solution(times,10)== [0, 1]

    times =[[0, 20, 20, 20, -1],
          [90, 0, 20, 20, 0],
          [90, 30, 0, 20, 0],
          [90, 30, 20, 0, 0],
          [-1, 30, 20, 20, 0]] #, 0, [0, 1, 2])

    assert solution(times, 0)== [0, 1, 2]

    times=[[0, 10, 10, 10, 1],
          [0, 0, 10, 10, 10],
          [0, 10, 0, 10, 10],
          [0, 10, 10, 0, 10],
          [1, 1, 1, 1, 0]] #, 5, [0, 1])

    assert solution(times, 5) == [0, 1]

    times = [[2, 2],
          [2, 2]] #, 5, [])

    assert solution(times,5) == []

    times=[[0, 10, 10, 1, 10],
          [10, 0, 10, 10, 1],
          [10, 1, 0, 10, 10],
          [10, 10, 1, 0, 10],
          [1, 10, 10, 10, 0]] #, 6, [0, 1, 2])

    assert solution(times, 6) == [0, 1, 2]

    times=[[1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1]] #, 1, [])

    assert solution(times,1) == []

    times=[[0, 0, 1, 1, 1],
          [0, 0, 0, 1, 1],
          [0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]] #, 0, [0, 1, 2])

    assert solution(times,0) == [0, 1, 2]

    times=[[1, 1, 1, 1, 1],
          [-1, 1, 1, 1, 1],
          [-1, 1, 1, 1, 1],
          [-1, 1, 1, 1, 1],
          [-1, 1, 1, 1, 1]]  #, 1, [0, 1, 2])

    assert solution(times,1)== [0, 1, 2]

    times=[[0, 1, 5, 5, 5, 5],
          [5, 0, 1, 5, 5, 5],
          [5, 5, 0, 5, 5, -1],
          [5, 5, 1, 0, 5, 5],
          [5, 5, 1, 5, 0, 5],
          [5, 5, 1, 1, 1, 0]]
          #, 3, [0, 1, 2, 3])

    assert solution(times, 3)== [0, 1, 2, 3]

    times=[[0, 1, 5, 5, 5, 5, 5],
          [5, 0, 1, 5, 5, 5, 5],
          [5, 5, 0, 5, 5, 0, -1],
          [5, 5, 1, 0, 5, 5, 5],
          [5, 5, 1, 5, 0, 5, 5],
          [5, 5, 0, 5, 5, 0, 0],
          [5, 5, 1, 1, 1, 0, 0]]
         #  , 3, [0, 1, 2, 3, 4])

    assert solution(times,3)== [0, 1, 2, 3, 4]

    times = [[0, -1, 0, 9, 9, 9, 9, 9],  # Start
          [9, 0, 1, 9, 9, 9, 9, 9],  # 0
          [0, 9, 0, 0, 9, 9, 1, 1],  # 1
          [9, 9, 9, 0, 1, 9, 9, 9],  # 2
          [9, 9, 9, 9, 0, -1, 9, 9],  # 3
          [9, 9, 0, 9, 9, 0, 9, 9],  # 4
          [9, 9, -1, 9, 9, 9, 0, 9],  # 5
          [9, 9, 9, 9, 9, 9, 9, 0]] #,  # bulkhead
         #1, [0, 1, 2, 3, 4, 5])

    assert solution(times, 1)== [0, 1, 2, 3, 4, 5]

    times=[[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]  #, 0, [0, 1, 2])

    assert solution(times, 0)== [0, 1, 2]

    # times=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]#,
    #      #0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
    #
    # assert solution(times, 0)== [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

    # times=[[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #       [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #       [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    #       [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]#,
    #      #5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
    #
    # assert solution(times, 5) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]