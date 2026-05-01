# Brute and Better

'''def maxsubarray(nums):
    n = len(nums)
    max_sub = float('-inf')

    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += nums[j]

            max_sub = max(max_sub,sum)

    return max_sub

nums =  [2, 3, 5, -2, 7, -4]
print(maxsubarray(nums))'''

# Optimization


def max_subarray_with_indices(arr):
    n = len(arr)

    maxi = float('-inf')   # same as INT_MIN
    curr_sum = 0

    start = 0
    ans_start = -1
    ans_end = -1

    for i in range(n):
        # if current sum is 0, start new subarray
        if curr_sum == 0:
            start = i

        curr_sum += arr[i]

        # update maximum
        if curr_sum > maxi:
            maxi = curr_sum
            ans_start = start
            ans_end = i

        # reset if sum becomes negative
        if curr_sum < 0:
            curr_sum = 0

    return maxi, ans_start, ans_end


# Example
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
max_sum, start, end = max_subarray_with_indices(arr)

print("Max Sum:", max_sum)
print("Subarray:", arr[start:end+1])
print("Start Index:", start, "End Index:", end)

'''Complexity
Time: O(n) ✅ (single loop)
Space: O(1) ✅ (no extra space)'''


def max_subarray_with_indices(arr):
    curr_sum = arr[0]
    max_sum = arr[0]

    start = 0
    ans_start = 0
    ans_end = 0

    for i in range(1, len(arr)):
        # decide whether to start new subarray
        if arr[i] > curr_sum + arr[i]:
            curr_sum = arr[i]
            start = i
        else:
            curr_sum += arr[i]

        # update best result
        if curr_sum > max_sum:
            max_sum = curr_sum
            ans_start = start
            ans_end = i

    return max_sum, ans_start, ans_end









