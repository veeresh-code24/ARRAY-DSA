# Brute force

'''def largest_element(nums):
    nums.sort()
    return nums[-1]

nums = [3,3,6,1]
print(largest_element(nums))'''

# optimal

'''def largest_element(nums):
    n = len(nums)
    largest = nums[0]

    for i in range(1,n):
        if nums[i] > largest:
            largest = nums[i]

    return largest

# nums = [3,3,6,1]
nums = [8, 10, 5, 7, 9]
print(largest_element(nums))'''


