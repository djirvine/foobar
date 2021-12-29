def intPart(n):
    # determine partitions of an integer

    # first time through yield n

    # ** Add Digit **
    # digit = n - sum of all digits in list
    # digit added can be at most equal to the previous digit
    # after adding digit (subject to max restriction), check sum
    # if n - sum of all digits in list is > 0, add digit
    # return new list

    # main loop runs while first element is > 1
    # if last digit added > 1 then decrement it, and add digit
        # yield list
    # else, remove last element
    # repeat until done

    # 1st run
    ip = [n]
    yield ip

    # function to add digit to the list
    # added digit cannot be greater than the last digit in the list
    def addDigit(ip):
        last = ip[-1]
        ni = n - sum(ip)
        if ni > last:
            ni = last
            ip += [ni]
            addDigit(ip)
        else:
            ip += [ni]
        return ip

    # generate list of partitions by continuously decrementing last element of list
    # when last element reaches 1, then remove it and repeat
    # stop when first element of list equals 1
    # this is the case of n ones
    while ip[0] > 1:
        if ip[-1] > 1:
            ip[-1] -= 1
            addDigit(ip)
            yield ip
        else:
            ip.pop()

if __name__ == "__main__":

    for e in intPart(5):
        print e

    # 5
    # 4 1
    # 3 2
    # 3 1 1
    # 2 2 1
    # 2 1 1 1
    # 1 1 1 1 1