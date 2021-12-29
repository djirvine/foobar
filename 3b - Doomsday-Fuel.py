def solution(m):
    # Your code here

    # function to print out matrix
    def pm(m):
        for row in m:
            print(row)
        print

    def gauss_jordan(m):

        # create new matrix with Identity matrix on the right
        for i, j in enumerate(m):
            m[i] += [float(n == i) for n in range(len(m))]

        # get size of matrix
        (h, w) = (len(m), len(m[0]))

        # cycle through the matrix from the top left
        for y in range(0, h):

            # set maxrow to the top row initially
            maxrow = y

            # search all rows below current row for row with biggest leading element (i.e. the leftmost element)
            for y2 in range(y + 1, h):
                # check leftmost element, stepping in each time through
                if abs(m[y2][y]) > abs(m[maxrow][y]):
                    maxrow = y2

            # swap row with max leading element with current top row
            (m[y], m[maxrow]) = (m[maxrow], m[y])

            # cycle through rows below current top row and eliminate leading elements by subtracting multiple of the
            # current top row (i.e. create zeros in the lower left)
            for y2 in range(y + 1, h):
                # calculate coefficient to use to scale top row for subtraction
                c = m[y2][y] / m[y][y]  # current row leading element / top row leading element

                # subtract a scaled version of each element in the current top row from each element in the active row
                for x in range(y, w):
                    m[y2][x] -= m[y][x] * c

            # now loop back and move down one and right one

        # Creates zeros in the upper right to diagonalize the matrix
        # start from lower right
        for y in range(h - 1, 0 - 1, -1):

            # get coefficient of leading element of the bottom row
            c = m[y][y]

            # modify rows from top down
            for y2 in range(0, y):

                # modify elements to the right only (elements to the left are not impacted as leading element
                # coefficients are zero)
                for x in range(w - 1, y - 1, -1):
                    # subtract bottom row (times the ratio of the top to the bottom row leading elements) from the
                    # current row (working top down)
                    m[y2][x] -= m[y][x] * m[y2][y] / c

            # Final step is to normalize leading coefficient to create the Identity matrix on the left
            # normalize the current bottom row (starting with the leading element, by dividing by the leading element value)

            m[y][y] /= c
            for x in range(h, w):  # Normalize row y
                m[y][x] /= c

            # loop back, next cycle will move up one row and over 1 to the left for leading element

        # strip off the Identity matrix on the left
        m = [i[len(m):] for i in m]

        return m

    def norm(m):
        for i in range(len(m)):

            m[i] = [m[i][n] / float(sum(m[i])) for n in range(len(m))] if sum(m[i]) > 0 else [1.0 * m[i][n] for n in
                                                                                          range(len(m))]

    def fundamental(m):
        for i in range(len(m)):
            for j in range(len(m)):
                m[i][j] = 1.0 - m[i][j] if i == j else -m[i][j]

    term = []
    for i, row in enumerate(m):
        if sum(row) == 0:
            term.append(i)

    norm(m)

    fundamental(m)

    m = gauss_jordan(m)

    # pm(m)

    answer = []

    eps = 1e-4

    for i in range(1, 200):
        test = [(m[0][n] * i % 1 < eps or 1.0 - m[0][n] * i % 1 < eps) for n in term]
        # print [(m[0][n] * i) for n in term] + [i]
        if sum(test) == len(term):
            answer = [int(round(m[0][n] * i)) for n in term] + [i]
            break

    return answer

m = [
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]

print solution(m)

assert (
        solution([
            [0, 2, 1, 0, 0],
            [0, 0, 0, 3, 4],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]) == [7, 6, 8, 21]
)

assert (
        solution([
            [0, 1, 0, 0, 0, 1],
            [4, 0, 0, 3, 2, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]) == [0, 3, 2, 9, 14]
)

assert (
    solution([
            [1, 2, 3, 0, 0, 0],
            [4, 5, 6, 0, 0, 0],
            [7, 8, 9, 1, 0, 0],
            [0, 0, 0, 0, 1, 2],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]) == [1, 2, 3]
)
assert (
        solution([
            [0]
        ]) == [1, 1]
)

assert (
    solution([
            [0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
            [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
            [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
            [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]) == [1, 2, 3, 4, 5, 15]
)

assert (
        solution([
            [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
            [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
            [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
            [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
            [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]) == [4, 5, 5, 4, 2, 20]
)

assert (
        solution([
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]) == [1, 1, 1, 1, 1, 5]
)

assert (
        solution([
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]) == [2, 1, 1, 1, 1, 6]
)

assert (
        solution([
            [0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
            [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
            [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]) == [6, 44, 4, 11, 22, 13, 100]
)

assert (
        solution([
            [0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
            [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
            [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
            [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
            [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]) == [1, 1, 1, 2, 5]
)