# # Brute force

# '''def longest_substring(s):
#     n = len(s)
#     max_len = 0

#     for i in range(n):
#         visited = [0]*256
#         for j in range(i,n):
#             if visited[ord(s[j])] == 1:
#                 break

#             visited[ord(s[j])] = 1

#             max_len = max(max_len,j-i+1)

#     return max_len

# s = "abcabcbb"
# s = "bbbbbb"
# s = "pwwkew"
# s = "cadbzabcd"
# print(longest_substring(s))'''

# # Brute force

# '''def longest_substring(s):
#     n = len(s)
#     max_len = 0

#     for i in range(n):
#         hashset = set()
#         for j in range(i,n):
#             if s[j] in hashset:
#                 break
#             hashset.add(s[j])

#             max_len = max(max_len, j-i+1)

#     return max_len

# s = "abcabcbb"
# s = "bbbbbb"
# s = "pwwkew"
# s = "cadbzabcd"
# print(longest_substring(s))'''

# # Optimization

# # def longest_substring(s):
# #     n = len(s)
# #     left,right,max_len = 0,0,0
# #     hashset = [-1]*256

# #     while right < n:
# #         if hashset[ord(s[right])] != -1:
# #             left = max(hashset[ord(s[right])]+1,left)

# #         max_len = max(right-left+1,max_len)

# #         hashset[ord(s[right])] = right
# #         right += 1

# #     return max_len
 


# # s = "abcabcbb"
# # s = "bbbbbb"
# # s = "pwwkew"
# # s = "cadbzabcd"
# # print(longest_substring(s))


# # Better Optimization

# def longest_substring(s):
#     last_seen = {}
#     left = 0
#     max_len = 0

#     for right in range(len(s)):
#         if s[right] in last_seen:
#             left = max(last_seen[s[right]] + 1, left)

#         # last_seen[s[right]] = right
#         max_len = max(max_len, right - left + 1)
#         last_seen[s[right]] = right

#     return max_len

# # s = "abcabcbb"
# # s = "bbbbbb"
# # s = "pwwkew"
# s = "cadbzabcd"
# print(longest_substring(s))



