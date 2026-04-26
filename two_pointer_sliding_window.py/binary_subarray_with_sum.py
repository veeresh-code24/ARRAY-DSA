# def binary_subarray_with_sum(nums,goal):
#     n = len(nums)
#     count = 0

#     for i in range(n):
#         pre_sum = 0
#         for j in range(i,n):
#             pre_sum += nums[j]

#             if pre_sum == goal:
#                 count += 1

#     return count
                
# # nums = [1,0,1,0,1]
# # goal = 2
# nums = [0,0,0,0,0]
# goal = 0

# print(binary_subarray_with_sum(nums,goal))


def binary_subarray_with_sum(nums,goal):
    n = len(nums)
    count = 0
    pre_sum = 0
    d = {0:1}

    for num in nums:
        pre_sum += num

        if pre_sum - goal in d:
            count += d[pre_sum - goal]

        d[pre_sum] = d.get(pre_sum,0)+1

    return count




                
# nums = [1,0,1,0,1]
# goal = 2
nums = [0,0,0,0,0]
goal = 0

print(binary_subarray_with_sum(nums,goal))
