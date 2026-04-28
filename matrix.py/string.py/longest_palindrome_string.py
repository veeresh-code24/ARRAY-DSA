def longest_palindrome_string(s):
    n = len(s)
    arr = []

    for i in range(n):
        for j in range(i,n):
            if s[j] == s[::-1]:
                arr.append(s[j])




    return arr
s = "babad"
print(longest_palindrome_string(s))








