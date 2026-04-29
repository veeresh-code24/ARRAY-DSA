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

def fruits_basket(fruits):
    n = len(fruits)
    mapp = {}
    max_len = 0
    left = 0

    for right in range(n):
        mapp[fruits[right]] = mapp.get(fruits[right],0)+1

        if len(mapp) > 2:
            mapp[fruits[left]] -= 1

            if mapp[fruits[left]] == 0:
                del mapp[fruits[left]]

            left += 1

        max_len = max(max_len, right-left+1)

    return max_len

    



 


# fruits = [1, 2, 3, 2, 2]
fruits = [1, 2, 1]
print(fruits_basket(fruits))
