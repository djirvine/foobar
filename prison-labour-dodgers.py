
def solution(x, y):

    #sort the lists
    x.sort()
    y.sort()

    #swap lists so that y is the longest
    if len(x) > len(y):
        y,x = x,y

    for e in range(len(x)):
        if y[e] != x[e]:
            print y[e]
            return y[e]  # return first element in y that doesn't match x

    print y[len(x)]
    return y[len(x)]  # if this point reached,then the remaining element in y doesn't match, so return it

def solution2(x,y):
    # swap lists so that y is the longest
    if len(x) > len(y):
        y, x = x, y

    dodger = [prisoner not in x for prisoner in y]

    print y[dodger.index(True)]
    return y[dodger.index(True)]



x = [13, 5, 6, 2, 5]
y = [5, 2, 5, 13]
assert solution(x, y) == 6
assert solution2(x, y) == 6


x = [14, 27, 1, 4, 2, 50, 3, 1]
y = [2, 4, -4, 3, 1, 1, 14, 27, 50]

assert solution(x, y) == -4
assert solution2(x, y) == -4