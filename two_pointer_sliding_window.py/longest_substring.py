def longest_substring(s):
    n = len(s)
    j = 0

    for i in range(1,n):
        if s[i] == s[j]:
            return i









# s = "abcabcbb"
s = "bbbbbb"
s = "pwwkew"
print(longest_substring(s))