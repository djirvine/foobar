# Class for vertices
class V():
    def __init__(self):
        self.d = float("inf")  # shortest weighted distance to vertex

# Class for graph and related functions to solve max bunnies problem
class G():
    def __init__(self, AM):
        self.AM = AM  # adjacency matrix, gives transit times between vertices
        self.numV = len(AM)  # number of vertices
        self.V = [V() for i in range(self.numV)]  # array of vertices in graph
        self.lwp = [[[] for col in range(self.numV)] for row in range(self.numV)]  # initialize lowest weight path (lwp) matrix
        self.bulkhead = self.numV - 1  # store vertex number for bulkhead
        self.longestPath = []  # longest path found in time limit -> should contain the most bunnies

    # function for printing matrix nicely
    @classmethod
    def printAdjMatrix(cls, AM):
        for row in AM:
            print(row)
        print

    # Initialize distances for BellmanFord algorithm
    @classmethod
    def Initialize(cls, G, s):
        for v in G.V:
            v.d = float("inf")  # initialize distance for all vertices to infinity except for the source vertex
        G.V[s].d = 0

        return 0

    # Relaxation function for BellmanFord algorithm
    @classmethod
    def Relax(cls, u, v, G):
        if G.V[v].d > G.V[u].d + G.AM[u][v]:
            G.V[v].d = G.V[u].d + G.AM[u][v]

        return 0

    # Main BellmanFord algorithm
    @classmethod
    def BellmanFord(cls, G, s):

        # initialize all vertices
        G.Initialize(G, s)

        # iterate |V|-1 times and relax each vertex -> |V| is the number of vertices
        for i in range(len(G.AM)-1):
            for u, row in enumerate(G.AM):
                for v, col in enumerate(row):
                    if u != v:
                        G.Relax(u, v, G)

        # check for negative cycle paths
        for u, row in enumerate(G.AM):
            for v, col in enumerate(row):
                if G.V[v].d > G.V[u].d + G.AM[u][v]:
                    return False

        # no negative cycles found
        return True

    # Brute force method to examine all paths
    @classmethod
    def buildPath(cls, G, current, timeRemaining, path, count, done):

        # only run if feasible solution for all bunnies not yet found
        if not done:

            count += 1  # variable to limit depth of search

            # try all vertices from current vertex except self
            for nextVertex in set(range(G.numV)) - {current}:

                # check if possible to get back to the bulk head after with time >=0 after moving to nextVertex
                if timeRemaining - G.lwp[current][nextVertex] - G.lwp[nextVertex][G.bulkhead] >= 0:

                    # limit depth of search
                    if count > 7:
                        break
                    # recursively search vertices with decreased remaining time
                    G.buildPath(G, nextVertex, timeRemaining - G.lwp[current][nextVertex], path+[nextVertex], count, done)

            # use set to check longest path containing bunnies only and ignoring repeated visits to the same bunny
            currentLongestPath = set(path) - set([0, G.bulkhead])

            # store longest path found
            if len(currentLongestPath) > len(G.longestPath):
                G.longestPath = currentLongestPath

            # if we have picked up all possible bunnies then stop searching
            if len(G.longestPath) == G.numV-2:
                done = True

            # return best path found
            return G.longestPath


# main function to find maximum number of bunnies that can be picked up
def solution(times, time_limit):

    # print starting matrix of transit times
    # G.printAdjMatrix(times)

    # number of vertices
    numV = len(times)

    # trivial case, no bunnies
    if numV == 2:
        # print "No bunnies to pickup"
        bunniesPickedUp = []
        # print "************\nBunnies Picked Up = ", bunniesPickedUp, "\n************\n\n"

        return bunniesPickedUp

    # initialize graph using transit time matrix
    g = G(times)

    # use BellmanFord to convert times matrix into a lowest weighted path (lwp) matrix
    for i, row in enumerate(g.lwp):
        # call BellmanFord for each possible starting point, to generate each row of lwp matrix
        if not G.BellmanFord(g, i):
            # negative cycle present, therefore have infinite time and can collect all bunnies
            # print "Negative cycle -> infinite time!!! Can pick up all the bunnies"
            bunniesPickedUp = list(range(numV - 2))
            # print "************\nBunnies Picked Up = ", bunniesPickedUp, "\n************\n\n"

            return bunniesPickedUp

        # build each row the lowest weighted path matrix
        for j, col in enumerate(g.lwp):
            g.lwp[i][j] = g.V[j].d

    # print out lwp matrix
    # G.printAdjMatrix(g.lwp)

    # Brute force iteration through all valid paths, saving longest path along the way

    # set starting point
    current = 0

    # set initial path
    path = [current]

    # set initial time remaining
    timeRemaining = time_limit

    # call recursive brute force path finding function
    path = G.buildPath(g, current, timeRemaining, path, 0, False)

    # convert result from set to list
    path = list(path)

    # initialize list for final output
    bunniesPickedUp = []

    # convert vertex numbers to bunny numbers
    for v in path:
        bunniesPickedUp.append(v-1)

    #print "************\nBunnies Picked Up = ", bunniesPickedUp,"\n************\n\n"

    # return list of bunnies picked up
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