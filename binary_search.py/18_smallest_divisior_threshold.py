# Brute Force

'''import math

def smallest_divisor(nums, threshold):

    for divisor in range(1, max(nums)+1):

        total = 0

        for num in nums:
            total += math.ceil(num / divisor)

        if total <= threshold:
            return divisor

nums = [1,2,5,9]
threshold = 6

print(smallest_divisor(nums, threshold))'''

# Time complexity -- O(max(nums) * n)
# Space Complexity -- O(N)

# Optimization Approach

import math

def smallest_divisor(nums, threshold):

    low, high = 1, max(nums)
    ans = high

    while low <= high:

        mid = (low + high) // 2

        total_sum = 0

        for num in nums:
            total_sum += math.ceil(num / mid)

        if total_sum <= threshold:

            ans = mid
            high = mid - 1

        else:
            low = mid + 1

    return ans


nums = [44,22,33,11,1]
threshold = 5

print(smallest_divisor(nums, threshold))

# Tc = O(n * log(max(nums)))
# Sc = O(1)

