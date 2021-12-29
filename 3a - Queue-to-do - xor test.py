def getxor(s, n):

    if s % 2 == 0:
        xor = [n, 1, n + 1, 0]

    else:
        xor = [s, s ^ n, s-1, (s-1) ^ n]

    i = (n - s) % 4
    x = xor[i]
    return x

def solution(start, length):
    xor = 0
    for r in range(length):
        row=[]
        # for c in range (start + r * length, start + r * length + (length - r )):
        #     row.append(c)
        # print(row)
        s = start + r * length
        n = s + length - r - 1
        x = getxor(s, n)
        # print(f"s = {s}, n = {n}, x = {x}")
        xor ^= x
        # print("===")
    # print(f"xor = {xor}")
    return xor


# print table of even and odd starting points to see xor pattern

for s in range(2,12,2):
    print()
    # s = 2
    prev = 0
    prev2 = 0
    for i in range(s, s+32):
        n = i
        n2 = i+1

        n ^= prev
        n2 ^= prev2

        print(f"n {i:4} {i:08b} {n:4} {n:08b} {getxor(s, i):08b}        n {i+1:4} {i+1:08b} {n2:4} {n2:08b} {getxor(s+1, i+1):08b}")
        prev = n
        prev2 = n2


length = 4
start = 17

test = [[0, 3], [17, 4], [1, 1], [7, 1]]

for t in test:
    print(f"start = {t[0]}, length = {t[1]} -> XOR = {solution(t[0], t[1])}")
