# Brute

'''def count_subarray(nums,k):
    n = len(nums)
    count = 0

    for i in range(n):
        total = 0
        for j in range(i,n):
            total += nums[j]

            if total == k:
                count += 1
    return count
nums = [1, 1, 1]
k = 2
print(count_subarray(nums,k))'''


def count_subarray(nums,k):
    n = len(nums)
    d = {0:1}
    prefix_sum = 0
    count = 0

    for num in nums:
        prefix_sum += num

        if prefix_sum-k in d:
            count += d[prefix_sum-k]

        d[prefix_sum] = d.get(prefix_sum,0)+1

    return count

nums = [1, 1]
k = 2
print(count_subarray(nums,k))


