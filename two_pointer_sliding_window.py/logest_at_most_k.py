# Brute Force

'''def longest_substring_at_k(s,k):
    n = len(s)
    max_len = 0

    for i in range(n):
        hash = {}
        for j in range(i,n):
            hash[s[j]] = hash.get(s[j],0)+1

            if len(hash) > k:
                break
                
                
                
            max_len = max(max_len,j-i+1)


    return max_len

 
# s = "aababbcaacc"
s = "abcddefg"
k = 3
# k = 2
print(longest_substring_at_k(s,k))'''

# Better 

def longest_substring_at_k(s,k):
    n = len(s)
    mapp = {}
    left = 0
    max_len = 0

    for right in range(n):
        mapp[s[right]] = mapp.get(s[right], 0)+1


        while len(mapp) > k:
            mapp[s[left]] -= 1
            if mapp[s[left]] == 0:
                del mapp[s[left]]

            left += 1

        max_len = max(max_len,right-left+1)

    return max_len

# s = "aababbcaacc"
# s = "abcddefg"
# k = 3
# k = 2
s = "abccab"
k = 4
print(longest_substring_at_k(s,k))
