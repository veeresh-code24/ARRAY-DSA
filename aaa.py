# def longest_substring(s):
#     n = len(s)
#     left = 0
#     max_len = 0
#     st = {}

#     for right in range(n):
#         if s[right] in st:
#             left = max(st[s[right]]+1,left)

#         max_len = max(max_len,right-left+1)
#         st[s[right]] = right

#     return max_len

# # s = "abcabcbb"
# # s = "bbbbb"
# s = "pwwkew"
# print(longest_substring(s))

def max_consecutive(nums,k):
    n = len(nums)
    max_len = 0

    for i in range(n):
        count = 0
        for j in range(i,n):
            if nums[j] == 0:
                count += 1


            if count > k:
                break


            max_len = max(max_len,j-i+1)

    return max_len


# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k = 3
# print(max_consecutive(nums,k))

# def max_consecutive(nums,k):
#     n = len(nums)
#     max_len = 0
#     zero = 0
#     left = 0

#     for right in range(n):
#         if nums[right] == 0:
#             zero += 1


#         while zero > k:
#             if nums[left] == 0:
#                 zero -= 1

#             left += 1
        
#         max_len = max(max_len,right-left+1)

#     return max_len


# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k = 3
# print(max_consecutive(nums,k))


# def fruits_basket(fruits):
#     n = len(fruits)
#     max_len = 0


#     for i in range(n):
#         basket = {}
#         for j in range(i,n):
#             basket[fruits[j]] = basket.get(fruits[j],0)+1

#             if len(basket) > 2:
#                 break

#             max_len = max(max_len,j-i+1)

#     return max_len

# # fruits = [1, 2, 3, 2, 2]
# fruits = [1, 2, 1]
# print(fruits_basket(fruits))

# def fruits_basket(fruits):
#     n = len(fruits)
#     mapp = {}
#     max_len = 0
#     left = 0

#     for right in range(n):
#         mapp[fruits[right]] = mapp.get(fruits[right],0)+1

#         if len(mapp) > 2:
#             mapp[fruits[left]] -= 1

#             if mapp[fruits[left]] == 0:
#                 del mapp[fruits[left]]

#             left += 1

#         max_len = max(max_len, right-left+1)

#     return max_len

    



 


# # fruits = [1, 2, 3, 2, 2]
# fruits = [1, 2, 1]
# print(fruits_basket(fruits))


# def longest_substring_char_repl(s,k):
#     n = len(s)
#     max_len = 0

#     for i in range(n):
#         freq = {}
#         max_freq = 0
#         for j in range(i,n):
#             freq[s[j]] = freq.get(s[j],0)+1

#             max_freq = max(max_freq,freq[s[j]])

#             window_len = j-i+1
#             replace = (window_len-max_freq)

#             if replace <= k:
#                 max_len = max(max_len,window_len)

#     return max_len

# s = "AABABBA"
# # s = "ABAB"
# k = 1
# print(longest_substring_char_repl(s,k))

# def longest_substring_char_repl(s,k):
#     n = len(s)
#     mapp = {}
#     max_freq = 0
#     max_len = 0
#     left = 0

#     for right in range(n):
#         mapp[s[right]] = mapp.get(s[right],0)+1
#         max_freq = max(max_freq,mapp[s[right]])


#         while right-left+1-max_freq > k:
#             mapp[s[left]] -= 1
#             # if mapp[s[left]] == 0:
#             left += 1


#         max_len = max(max_len,right-left+1)

#     return max_len


# # s = "AABABBA"
# s = "ABAB"
# k = 2
# print(longest_substring_char_repl(s,k))

# def binary_sum(nums,goal):
#     n = len(nums)
#     count = 0

#     for i in range(n):
#         total = 0
#         for j in range(i,n):
#             total += nums[j]

#             if total == goal:
#                 count += 1
#             # else:
#                 # break


#     return count


# nums = [1,0,1,0,1]
# # nums = [0,0,0,0,0]
# goal = 2
# print(binary_sum(nums,goal))

# def binary_sum(nums,goal):
#     n  = len(nums)
#     d= {0:1}
#     pre_sum = 0
#     count = 0

#     for i in range(n):
#         pre_sum += nums[i]

#         if pre_sum - goal in d:
#             count += d[pre_sum-goal]

#         d[pre_sum] = d.get(pre_sum,0)+1

#     return count

# # nums = [1,0,1,0,1]
# nums = [0,0,0,0,0]
# goal = 0
# print(binary_sum(nums,goal))

def binary_sum(nums,goal):
    n = len(nums)
    if goal < 0:
        return 0
    
    pre_sum = 0
    left = 0
    count = 0

    for right in range(n):
        pre_sum += nums[right]


        while pre_sum > goal:
            pre_sum -= nums[left]
            left += 1

        count += (right -left +1)
    return count

def at_most(nums,goal):
    return binary_sum(nums,goal) - binary_sum(nums,goal-1)



# nums = [1,0,1,0,1]
nums = [0,0,0,0,0]
goal = 0
print(at_most(nums,goal))