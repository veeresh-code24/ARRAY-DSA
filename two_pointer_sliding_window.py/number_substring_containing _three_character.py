# Brute Force

'''def substr_contai_three(s):
    n = len(s)
    count = 0

    for i in range(n):
        hash = {'a':0, 'b':0, 'c':0}
        for j in range(i,n):
            # hash[s[j]] = hash.get(s[j],0)+1
            hash[s[j]] += 1


            if hash['a'] > 0 and hash['b'] > 0 and hash['c'] > 0:

                count += 1

    return count

s = "abcabc"
# s = "aaacb"
# s = "abc"
print(substr_contai_three(s))'''


def substr_contai_three(s):
    n = len(s)
    freq = [0,0,0]
    res = 0
    left = 0

    for right in range(n):
        freq[ord(s[right])- ord('a')] += 1

        while freq[0] > 0 and freq[1] > 0 and freq[2] > 0:
            res += len(s) - right


            freq[ord(s[left]) - ord('a')] -= 1

            left += 1

    return res



# s = "abcabc"
s = "aaacb"
# s = "abc"
print(substr_contai_three(s))


