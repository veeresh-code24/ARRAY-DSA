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

# def longest_repeating_replacement(s,k):
#     max_len = 0
    
#     for i in range(len(s)):
#         freq = [0] * 26
#         max_freq = 0

#         for j in range(i,len(s)):
#             freq[ord(s[j]) - ord('A')] += 1

#             max_freq = max(freq[ord(s[j])-ord('A')],max_freq)

#             window_len = j-i+1

#             replace = window_len  - max_freq

#             if replace <= k:
#                 max_len = max(max_len,window_len)

#     return max_len


# s = "AABABBA"
# k = 1
# # s = "ABB"
# # k = 1
# print(longest_repeating_replacement(s,k))

# dictionary optimal

class Solution:
    # Function to return the length of the longest substring that can be made of repeating characters
    # by replacing at most k characters
    def characterReplacement(self, s: str, k: int) -> int:

        # Dictionary to count frequency of characters in current window
        freq = {}

        # Left pointer of sliding window
        left = 0

        # Stores max frequency of any char in current window
        max_freq = 0

        # Stores result
        max_len = 0

        # Traverse through each character with right pointer
        for right in range(len(s)):

            # Increase frequency of current character
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Update the max frequency in current window
            max_freq = max(max_freq, freq[s[right]])

            # If window is invalid (more than k replacements)
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            # Update max_len with current valid window size
            max_len = max(max_len, right - left + 1)

        return max_len

# Driver code
if __name__ == "__main__":
    sol = Solution()
    s = "AABABBA"
    k = 1
    print(sol.characterReplacement(s, k))

# Optimal


def longest_repeating_replacement(s,k):

    n = len(s)
    freq = [0] * 26
    max_freq = 0
    max_len = 0
    left = 0

    for right in range(n):
        freq[ord(s[right]) - ord('A')] += 1
        max_freq = max(max_freq,freq[ord(s[right])-ord('A')])

        if right - left+1 -max_freq > k:
            freq[ord(s[left])-ord('A')] -= 1
            left += 1

        if right -left+1 - max_freq <= k:
            max_len = max(max_len, right-left+1)

    return max_len



s = "AABABBA"
k = 1
# s = "ABB"
# k = 1
print(longest_repeating_replacement(s,k))