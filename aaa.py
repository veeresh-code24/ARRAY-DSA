'''def longest_subarray(nums,k):
    n = len(nums)

    max_long = 0

    for i in range(n):
        curr_sum = 0
        for j in range(i,n):
            curr_sum += nums[j]

            if curr_sum == k:
                max_long = max(max_long, j-i+1)

    return max_long



# nums = [10, 5, 2, 7, 1, 9]
# k=15
nums = [-3, 2, 1]
k=6
print(longest_subarray(nums,k))


def longest_subarray(nums,k):
    n = len(nums)
    pre_sum = 0
    max_long = 0
    d = {0:-1}

    for i in range(n):
        pre_sum += nums[i]

        rem = pre_sum - k

        if rem in d:
            max_long = max(max_long, i-d[rem])

        if pre_sum not in d:
            d[pre_sum] = i

    return max_long


nums = [-3, 2, 1]
# nums = [10, 5, 2, 7, 1, 9]
k=6
print(longest_subarray(nums,k))'''


'''def longest_subarray(nums,k):
    n = len(nums)
    max_long = 0
    curr_sum  = 0
    left = 0

    for right in range(n):
        curr_sum += nums[right]

        if curr_sum > k:
            curr_sum -= nums[left]
            left += 1


        if curr_sum == k:
            max_long = max(max_long, right-left+1)



    return max_long

# nums = [-3, 2, 1]
nums = [10, 5, 2, 7, 1, 9]
k=15
print(longest_subarray(nums,k))'''

'''def two_sum(nums,target):

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

    return -1,-1

# nums = [2,7,11,15]
# target = 9
nums = [3,2,4]
target = 6

print(two_sum(nums,target))'''

'''def two_sum(nums,target):
    n = len(nums)
    d = {}

    for i in range(n):
        a = nums[i]
        res = target - nums[i]

        if res in d:
            return (d[res],i)


        d[a] = i



nums = [2,7,11,15]
target = 9
# nums = [3,2,4]
# target = 6

print(two_sum(nums,target))'''

'''def two_sum(nums,target):
    n = len(nums)

    left = 0
    right = n-1

    while left < right:
        sum = nums[right] + nums[left]

        if sum == target:
            return "Yes"

        elif sum < target:
            left += 1

        else:
            right -= 1

    return "No"




nums = [2,7,11,15]
target = 9
# nums = [3,2,4]
# target = 6

print(two_sum(nums,target))'''

'''def sort_colors(nums):
    n  = len(nums)

    count0=0
    count1 = 0
    count2 = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            count0 += 1

        elif nums[i] == 1:
            count1 += 1

        else:
            count2 += 1


    for i in range(count0):
        nums[i] = 0

    for i in range(count0, count0+count1):
        nums[i] = 1

    for i in range(count0+count1,n):
        nums[i] = 2

    return nums



# nums = [2,0,2,1,1,0]
nums = [2,0,1]
print(sort_colors(nums))'''

def sort_colors(nums):
    n  = len(nums)

    low = 0
    mid = 0
    high = n-1

    while mid <= high:
        if nums[mid] == 0:
            nums[low],nums[mid] = nums[mid],nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:
            nums[mid],nums[high] = nums[high],nums[mid]
            high -=1

    return nums


# nums = [2,0,2,1,1,0]
nums = [2,0,1]
print(sort_colors(nums))

