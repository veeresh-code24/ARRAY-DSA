# Brute and brute optimization

'''def longest_subarry(nums,k):
    n = len(nums)
    max_sum = 0

    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += nums[j]

            if sum == k:
                max_sum = max(max_sum,j-i+1)

    return max_sum
    
nums = [10, 5, 2, 7, 1, 9]
k=15
print(longest_subarry(nums,k))'''


# Better

'''def long_subarray(nums,k):
    n = len(nums)

    prefi_sum = 0
    max_len = 0
    d = {}

    for i in range(n):
        prefi_sum += nums[i]

        if prefi_sum == k:
            max_len = max(max_len,i+1)

        rem = prefi_sum - k

        if rem in d:
            length = i - d[rem]
            max_len = max(max_len,length)

        if rem not in d:
            d[prefi_sum] = i

    return max_len

nums = [10, 5, 2, 7,1,1, 9]
k=16

print(long_subarray(nums,k))'''


'''def long_subarray(nums, k):
    n = len(nums)
    prefi_sum = 0
    max_len = 0
    d = {0: -1}  # ✅ Key fix
    
    for i in range(n):
        prefi_sum += nums[i]
        
        rem = prefi_sum - k
        if rem in d:
            max_len = max(max_len, i - d[rem])
        
        if prefi_sum not in d:  # ✅ Store prefix, not rem
            d[prefi_sum] = i
    
    return max_len'''

# Optimization

def longest_sunarray(nums,k):
    n = len(nums)
    left = 0
    right = 0
    max_len = 0
    sum = nums[0]

    while right < n:
        while left <= right and sum > k:
            sum -= nums[left]

            left += 1

        if sum == k:
            max_len = max(max_len,right-left+1)

        right += 1

        if right < n:
            sum += nums[right]

    return max_len

nums = [10, 5, 2, 7,1,1, 9]
k=16

print(longest_sunarray(nums,k))

# little bit better
def longest_subarray(nums, k):
    n = len(nums)

    left = 0
    pre_sum = 0
    max_len = 0

    for right in range(n):
        pre_sum += nums[right]

        while left <= right and pre_sum > k:
            pre_sum -= nums[left]
            left += 1

        if pre_sum == k:
            max_len = max(max_len, right - left + 1)

    return max_len


nums = [10, 5, 2, 7, 1, 9]
k = 15
print(longest_subarray(nums, k))


 



        



