# # def longest(s):
# #     n = len(s)
# #     max_len = 0

# #     for i in range(n):
# #         visited = [0] * 256

# #         for j in range(i,n):
# #             if visited[ord(s[j])] == 1:
# #                 break

# #             visited[ord(s[j])] = 1

# #             max_len = max(max_len,j-i+1)

# #     return max_len


# # s = "abcabcbb"
# # # s = "bbb"
# # print(longest(s))

# # def longest_substring(s):
# #     n = len(s)
# #     max_len = 0

# #     for i in range(n):
# #         visited = [0]*256
# #         for j in range(i,n):
# #             if visited[ord(s[j])] == 1:
# #                 break

# #             visited[ord(s[j])] = 1
# #             max_len = max(max_len,j-i+1)

# #     return max_len

# # s = "abcabcbb"
# # # s = "bbbbbb"
# # # s = "pwwkew"
# # # s = "cadbzabcd"
# # print(longest_substring(s))

# # def longest_substring(s):
# #     n = len(s)
# #     hashset = [-1] * 256
# #     max_len = 0
# #     r = 0
# #     l = 0

# #     while r < n:
# #         if hashset[ord(s[r])] != -1:
# #             l = max(hashset[ord(s[r])]+1, l)


# #         max_len = max(max_len,r-l+1)
# #         hashset[ord(s[r])] = r
# #         r += 1

# #     return max_len

# # # s = "abcabcbb"
# # s = "bbbbbb"
# # # s = "pwwkew"
# # # s = "cadbzabcd"
# # print(longest_substring(s))

# # def maximum_conse(nums,k):
# #     n = len(nums)
# #     max_len = 0

# #     for i in range(n):
# #         zero = 0
# #         for j in range(i,n):
# #             if nums[j] == 0:
# #                 zero += 1

# #             if zero > k:
# #                 break

# #             max_len = max(max_len,j-i+1)

# #     return max_len



# # # nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# # nums = [1,1,1,0,0,0,1,1,1,1,0]
# # k = 2
# # # k = 3
# # print(maximum_conse(nums,k))

# def maximum_conse(nums,k):
#     n = len(nums)

#     left = 0
#     max_len = 0
#     zero = 0

#     for right in range(n):
#         if nums[right] == 0:
#             zero += 1


#         if zero > k:
#             if nums[left] == 0:
#                 zero -= 1

#             left += 1

#         max_len = max(max_len,right-left+1)

#     return max_len



# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# # nums = [1,1,1,0,0,0,1,1,1,1,0]
# # k = 2
# k = 3
# print(maximum_conse(nums,k))


# def fruit_basket(fruits):
#     n = len(fruits)
#     max_len = 0

#     for i in range(n):
#         dic = {}
#         for j in range(i,n):
#             dic[fruits[j]] = dic.get(fruits[j],0)+1

#             if len(dic) > 2:
#                 break

#             max_len = max(max_len,j-i+1)

#     return max_len





# fruits = [1, 2, 1]
# # fruits = [1, 2, 3, 2, 2]

# print(fruit_basket(fruits))

def fruit_basket(fruits):
    n = len(fruits)
    left = 0
    max_len = 0
    hash = {}

    for right in range(n):
        hash[fruits[right]] = hash.get(fruits[right],0)+1

        while len(hash) > 2:
            hash[fruits[left]] -= 1


            if hash[fruits[left]] == 0:
                del hash[fruits[left]]
            left += 1


        max_len = max(max_len,right-left+1)


    return max_len




fruits = [1, 2, 1]
# fruits = [1, 2, 3, 2, 2]

print(fruit_basket(fruits))


