# Brute Approach

'''def find_minimum_rot_sor(nums):
    min_val = nums[0]

    for i in range(len(nums)):
        if nums[i] < min_val:
            min_val = nums[i]

    return min_val

# nums = [3,4,5,1,2]
nums = [4,5,6,7,0,1,2]
print(find_minimum_rot_sor(nums))'''

# Optimal Approach

def find_minimum_rot_sor(nums):
    n = len(nums)
    ans = float('inf')
    low,high = 0,n-1

    while low <= high:

        mid = (low+high)//2

        if nums[low] <= nums[mid]:
            ans = min(ans,nums[low])
            low = mid+1

        else:
            ans = min(ans,nums[mid])
            high = mid-1

    return ans

# nums = [3,4,5,1,2]
nums = [4,5,6,7,0,1,2]
print(find_minimum_rot_sor(nums))


# Optimization 2

def find_minimum_rot_sor(nums):
    low,high = 0,len(nums)-1

    while low < high:
        mid = (low+high)//2

        if nums[mid] > nums[high]:
            low = mid+1

        else:
            high = mid


    return nums[low]



nums = [3,4,5,1,2]
# nums = [4,5,6,7,0,1,2]
print(find_minimum_rot_sor(nums))



