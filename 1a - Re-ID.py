def solution(i):
    # Your code here
    i = int(i)

    # build string of prime numbers at least 10,005 long
    prime = "2"
    l = 10000
    count = 1

    # search up to first 100,000 integers if needed
    for n in range(3, 100000):
        # loop through denominators from 2 to n-1
        for d in range(2, n):
            if n % d == 0:  # not prime, therefore goto next n
                break
            if d == n - 1:
                # if we reach the end then prime, therefore concatenate onto prime string
                prime += str(n)
                count += 1
        # check if prime is at least 10,005 characters
        if len(prime) >= l + 5:
            # print(f"found first {count} primes")
            # print(f"length or prime string = {len(prime)}")
            break
    # return 5 digit ID
    return prime[i:i + 5]