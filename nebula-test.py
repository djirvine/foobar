def answer(state, a=0, b=0, past=0, solutions=0, history=0):
    # print "on entry a=", a, "b=", b
    if(past==0):
        past=[[True] * (len(state[0])+1) for i in range(len(state)+1)]
        solutions = {}
        history = []
        print "initializing\n", past

    if(b==len(state[0])+1):
        # print "ending, b=",b,"a=",a
        print "ending, found solution -> past = ", past
        # print "history=", history
        return True

    res=0
    index=((a,b), tuple(history[-(len(state)+2):]))
    # print "index=",index, history
    if index in solutions:
        print "Been here before: index, sol[ind]=", index, solutions[index]
        return solutions[index]

    for cell in [True, False]:
        # either all True(c[0][0] and 1 cell) or all False (!c[0][0] and !1 cell)
        # print "a=", a, "b=", b, "a-1=", a-1,"b-1=",b-1
        # print past[a][b-1], past[a-1][b], past[a-1][b-1], state[a-1][b-1]
        # print "past=", past
        # print "state=", state
        if (not a or not b) or len(set([((past[a][b-1] + past[a-1][b]
            + past[a-1][b-1] + cell)==1), state[a-1][b-1]]))==1:
                history.append(cell)
                # print "history=", history
                past[a][b] = cell
                # print "past=",past
                # print "before entry a=", a, "b=", b
                res+=answer(state, a=(a+1)%(len(state)+1),
                        b=b+(a+1)//(len(state)+1), past=past,
                        solutions=solutions, history=history)
                # print "returning a=", a, "b=", b
                # print "history before pop", history
                history.pop()
                # print "history after  pop", history


    solutions[index]=res
    # print "res =", res
    # print "solutions=",solutions
    # print "history=", history
    # print "a=",a, "b=",b
    return res

g = [[True, False, True], [False, True, False], [True, False, True]]

print answer(g)

# g = [[False, True, True], [False, True, False], [True, True, True]]
#
# print answer(g)
