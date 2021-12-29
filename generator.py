def gen(n):
    i=0
    while i < n:
        yield i
        i+=1

x = gen(5)
for e in x:
    print e