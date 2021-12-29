def solution(s,l):
    q = []
    for add in range(l):
        for n in range(s, s + l - add):
            n = n + add * l
            if n > 2 * 10 ** 9:
                n = n - 1 - 2 * 10 ** 9
            q.append(n)
    x = q[0]
    if len(q) > 1:
       for i in range(1, len(q)):
            x = x ^ q[i]
            prev = x
    return x

print(solution(0, 3))
print(solution(17, 4))

print(solution(1, 1))
print(solution(2*10**9, 1))
l = 5


print(solution(2*10**9, l))