# brute approach

# def subarray(nums):
#     n = len(nums)
#     max_len = 0

#     for i in range(n):
#         sum = 0
#         for j in range(i,n):
#             sum += nums[j]

#             if sum == 0:
#                 max_len = max(max_len,j-i+1)

#     return max_len
# nums = [15,-2,2,-8,1,7,10,23]
# print(subarray(nums))

# optimization

def subarray_zer0(nums):
    n = len(nums)
    d = {}
    max_len = 0
    sum = 0

    for i in range(n):
        sum += nums[i]

        if sum == 0:
            max_len = max(max_len,i+1)

        else:
            if sum in d:
                length = i-d[sum]
                max_len = max(max_len, length)
            else:
                d[sum] = i

    return max_len

    
nums = [15,-2,2,-8,1,7,10,23]
print(subarray_zero(nums))

