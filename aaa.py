# def longest_subarray(nums,k):
#     n = len(nums)
#     d = {0:-1}
#     max_len = 0
#     prefix_sum = 0


#     for i in range(n):
#         prefix_sum += nums[i]

#         if prefix_sum-k in d:
#             max_len = max(max_len, i-d[prefix_sum-k])

#         if prefix_sum not in d:
#             d[prefix_sum] = i

#     return max_len

# # nums =  [10, 5, 2, 7, 1, 9]
# # k=15
# nums = [-3, 2, 1]
# k=6

# print(longest_subarray(nums,k))

# def two_sum(nums,target):
#     n = len(nums)

#     for i in range(n):
#         for j in range(i+1,n):
#             if nums[j] + nums[i] == target:
#                 return i,j

# nums = [2,7,11,15]
# target = 9
# print(two_sum(nums,target))

# def two_sum(nums,target):
#     n = len(nums)
#     d = {}

#     for i in range(n):
#         a = nums[i]
#         mpp = target - nums[i]
#         if mpp in d:
#             return d[mpp],i
        
#         d[a] = i


# # nums = [2,7,11,15]
# # target = 9
# nums = [3,3]
# target = 6
# print(two_sum(nums,target))

# def two_sum(nums,target):
#     n = len(nums)
#     right = n-1
#     left = 0
#     while left < right:
#         sum = nums[left] + nums[right]

#         if sum == target:
#             return "Yes"
        
#         elif sum < target:
#             left += 1

#         else:
#             right -= 1

#     return "No"

# nums = [2,7,11,15]
# target = 9
# # nums = [3,4]
# # target = 6
# print(two_sum(nums,target))

def longest_subarray(nums,k):
    n = len(nums)
    if n == 0:
        return 0

    left = 0
    right = 0
    max_len = 0
    prefix_sum = nums[0]

    while right < n:
        while left <= right and  prefix_sum > k:
            prefix_sum -= nums[left]
            left += 1

        if prefix_sum == k:
            max_len = max(max_len,right-left+1)

        right += 1

        if right < n:
            prefix_sum += nums[right]
    return max_len

nums = [10, 5, 2, 7, 1, 1, 9]
k=16 
print(longest_subarray(nums,k))


