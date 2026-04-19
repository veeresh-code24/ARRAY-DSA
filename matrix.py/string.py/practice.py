# def largest(nums):
#     nums.sort()
#     return nums[-1]



# nums = [1,-2,3,-1,89,3,92,23,12,21]

# print(largest(nums))


# def largest(nums):
#     n = len(nums)
#     largest = nums[0]

#     for i in range(n):
#         if nums[i] > largest:
#             largest = nums[i]

#     return largest






# nums = [1,-2,3,-1,-89,3,92,23,-12,21]

# print(largest(nums))



# def largest(nums):
#     n = len(nums)
#     nums.sort()
#     largest = nums[-1]

#     for i in range(n-1,-1,-1):
#         if nums[i] != largest:
#             return nums[i]

# nums = [1,-2,3,-1,89,3,92,23,12,21]

# print(largest(nums))
# def largest(nums):
#     n = len(nums)


#     largest = nums[0]
#     second = -1

#     for i in range(1,n):
#         if nums[i] > largest:
#             largest = nums[i]


#     for i in range(n):
#         if nums[i] < largest and nums[i] > second:
#             second = nums[i]

#     return second

# nums = [1,-2,3,-1,-89,3,92,23,12,21]

# print(largest(nums))

# def largest(nums):
#     n = len(nums)
#     largest = float('-inf')
#     second = float('-inf')

#     for i in range(n):
#         if nums[i] > largest:
#             second = largest
#             largest = nums[i]

#         elif nums[i] > second and nums[i] < largest:
#             second = nums[i]

#     return second

# nums = [1,-2,3,-1,-89,3,92,23,12,21]
# print(largest(nums))

# def linear_search(nums,target):
#     n = len(nums)

#     for i in range(n):
#         if nums[i] == target:
#             return i
        
#     return -1


# nums = [21,12,39,98,76,65]
# target = 98
# print(linear_search(nums,target))

def rotate_array(nums):
    n = len(nums)
    temp = nums[0]

    for i in range(1,n):
        nums[i-1] = nums[i]
    nums[-1] = temp

    return nums

nums = [1,2,3,4,5]
print(rotate_array(nums))

