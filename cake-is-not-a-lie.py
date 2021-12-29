def solution(s):

    l = len(s)

    for i in range(1, l-1):
        # print i
        if l%i == 0:
            # print s[0:i]
            if s[0:i] == s[i:2*i]:
                print "Found", s[0:i]
                print l/i
                return l/i


assert solution('abcabcabcabc') == 4

assert solution('abccbaabccba') == 2
