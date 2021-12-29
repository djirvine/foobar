import math
def solution(i):
    # Your code here
    i = int(i)

    # build string of prime numbers at least 10,004 long
    prime = "2"
    l = 10000
    count = 1

    # search up to first 100,000 integers if needed
    for n in range(3, 100000):
        
        # loop through denominators from 2 to sqrt(n)+1
        upper = math.ceil(math.sqrt(n))+1

        for d in range(2, upper):
            if n % d == 0:  # not prime, therefore goto next number
                break
            if d == upper - 1:
                # if we reach the end then prime, therefore concatenate onto prime string
                prime += str(n)
                count += 1
        # check if prime is at least 10,004 characters
        if len(prime) >= l + 5:
            # print(f"found first {count} primes")
            # print(f"length or prime string = {len(prime)}")
            break
    # return 5 digit ID
    return prime[i:i + 5]
