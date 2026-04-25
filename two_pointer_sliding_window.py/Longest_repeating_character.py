# Brute Force

'''def longest_repeating_replacement(s,k):
    n = len(s)
    max_len = 0

    for i in range(n):
        hash = [0] * 26
        max_freq = 0

        for j in range(i,n):
            hash[ord(s[j]) - ord('A')] += 1

            max_freq = max( hash[ord(s[j]) - ord('A')], max_freq)

            window_len = j-i+1

            replace = window_len - max_freq

            if replace <= k:
                max_len = max(max_len,window_len)


    return max_len


# s = "AABABBA"
# k = 1
s = "ABB"
k = 2
print(longest_repeating_replacement(s,k))'''

def longest_repeating_replacement(s,k):
    max_len = 0
    
    for i in range(len(s)):
        freq = [0] * 26
        max_freq = 0

        for j in range(i,len(s)):
            freq[ord(s[j]) - ord('A')] += 1

            max_freq = max(freq[ord(s[j])-ord('A')],max_freq)

            window_len = j-i+1

            replace = window_len  - max_freq

            if replace <= k:
                max_len = max(max_len,window_len)

    return max_len


s = "AABABBA"
k = 1
# s = "ABB"
# k = 1
print(longest_repeating_replacement(s,k))