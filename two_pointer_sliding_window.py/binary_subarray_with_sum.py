#Better

'''def binary_subarray_with_sum(nums,goal):
    n = len(nums)
    count = 0

    for i in range(n):
        pre_sum = 0
        for j in range(i,n):
            pre_sum += nums[j]

            if pre_sum == goal:
                count += 1

    return count
                
# nums = [1,0,1,0,1]
# goal = 2
nums = [0,0,0,0,0]
goal = 0

print(binary_subarray_with_sum(nums,goal))'''

# Better

'''def binary_subarray_with_sum(nums,goal):
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

print(binary_subarray_with_sum(nums,goal))'''


# Optimal Solution Tc-- O(2n).  Sc---0(1)

'''def binary_subarray(nums,goal):
    n = len(nums)
    if goal < 0:
        return 0

    left = 0
    count = 0
    pre_sum = 0

    for right in range(n):
        pre_sum += nums[right]

        while pre_sum > goal:
            pre_sum -= nums[left]
            left += 1

        count += right - left+1

    return count

def exact_sum(nums,goal):
    return binary_subarray(nums,goal) - binary_subarray(nums,goal-1)
    


nums = [1,0,1,0,1]
goal = 2
print(exact_sum(nums,goal))'''