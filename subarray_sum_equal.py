# def subarray_aub_equal_k(nums,k):

#     n = len(nums)
#     count = 0

#     for i in range(n):
#         total = 0
#         for j in range(i,n):
#             total += nums[j]

#             if total == k:
#                 count += 1



#     return count

# nums = [1,1,1]
# k = 2
# print(subarray_aub_equal_k(nums,k))

def subarray_aub_equal_k(nums,k):
    n = len(nums)
    prefix_sum = 0
    count = 0
    hash = {0:1}

    for num in nums:
        prefix_sum += num

        if prefix_sum -k in hash:
            count  += hash[prefix_sum-k]

        hash[prefix_sum] = hash.get(prefix_sum,0) + 1


    return count

        


nums = [3,1,2,4]
k = 6
print(subarray_aub_equal_k(nums,k))