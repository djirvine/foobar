import math
# Uncached fibonacci sum
# def fibo_sum(n):
#     if n == 1:
#         # print(n)
#         return 1
#     elif n == 2:
#         # print(n)
#         return 2
#     else:
#
#         return fibo_sum(n-2) + fibo_sum(n-1) + 1

# Cached fibonacci sum
def fibo_sum(n): # n = [n, sum(n), sum(n-1)]
    # if no cached values available
    if n[1] == None and n[2] == None:
        if n[0] == 1:
            # print(n)
            return [1, 1, 0]
        elif n[0] == 2:
            # print(n)
            return [2, 2, 1]
        else:
            fs2 = fibo_sum([n[0]-2, None, None])
            fs1 = fibo_sum([n[0]-1, n[2], None])
            return [n[0], fs2[1] + fs1[1] + 1, fs1[1]]
    else:
        # print(f"Using cache - {n}")
        return [n[0], n[1] + n[2] + 1, n[1]]


def solution(n):
    # generous is based on powers of 2
    # stingy is just the fibonacci sequence

    # Sum of powers of first n powers of 2 is 2^n -1
    # fibonacci sequence f(n) = f(n-1) + f(n-2), f(1) =1 f(2) =1
    # Sum of fibonacci numbers fs(n) = fs(n-1) + fs(n-2) + 1 fs(1) = 1 fs(2) =2
    # largest payout is 10^9
    # series of n less than 10^2
    # int(log10(10^9)/log10(2)) = int(9/log(2)) = 29.9 = 29
    # print(f"Max LAMBS payout = {n}")
    generous = int(math.log(n, 2))
    # print(f"min hm = {generous}, LAMBS tot = {2**generous - 1}")

    stingy = generous
    fs = fibo_sum([stingy, None, None])
    loop = True
    while fs[1] <= n:
        ps = stingy
        prev = fs
        stingy +=1
        fs = fibo_sum([stingy,prev[1], prev[2]])

    # print(f"max hm = {ps}, LAMBS tot = {prev[1]}, diff={ps - generous}")
    return ps - generous
# test cases
# solution(10)
# print("***********")
# solution(143)

# print("***********")
# solution(2047)

# print("***********")
# solution(2**20)

# print("***********")
# solution(10**9)

