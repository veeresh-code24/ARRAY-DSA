# Brute
# def duplicate_number(nums):
#     n = len(nums)

#     for i in range(n):
#         num = nums[i]
#         count = 0
#         for j in range(n):
#             if nums[j] == num:
#                 count += 1

        
#         if count > 1:
#             return num
        
# # nums = [3,1,3,4,2]
# nums = [1,3,4,2,2]
# print(duplicate_number(nums))

# Better

# def duplicate_number(nums):
#     n = len(nums)
#     d = {}

#     for i in range(n):
#         if nums[i] not in d:
#             d[nums[i]] = 1
#         else:
#             d[nums[i]] += 1

#     for key,value in d.items():
#         if value > 1:
#             return key


        
# nums = [3,1,3,4,2]
# # nums = [1,3,4,2,2]
# print(duplicate_number(nums))

# optimized Better
'''def duplicate_number(nums):
    d = {}

    for num in nums:
        if num in d:
            return num
        d[num] = 1
        
nums = [3,1,3,4,2]
nums = [1,3,4,2,2]
print(duplicate_number(nums))'''


# OPtimized.  
# Using Floyd’s Cycle Detection (Best Solution)

def duplicate_number(nums):
    n = len(nums)

    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


nums = [3,1,3,4,2]
nums = [1,3,4,2,2]
print(duplicate_number(nums))





