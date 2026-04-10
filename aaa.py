def longest_subarry(nums,k):
    n = len(nums)
    max_sum = 0

    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += nums[j]

            if sum == k:
                max_sum = max(max_sum, j-i+1)

    return max_sum

nums = [10,5, 2, 7, 1, 9]
k=15
print(longest_subarry(nums,k))

