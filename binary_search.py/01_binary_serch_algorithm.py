# Linear search

'''def linear_search(nums,target):
    n = len(nums)

    for i in range(n):
        if nums[i] == target:
            return i
        
    return -1


nums = [1,2,3,3,5,8,8,10,10]
target = 9
print(linear_search(nums,target))'''

# Time Complexity: O(n)
# Space Complexity: O(1)

# Binary serach

'''def binary_search(nums,target):
    n = len(nums)

    low,high = 0, n-1

    while low <= high:
        mid  = (low+high)//2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] > target:
            high = mid-1

        else:
            low = mid+1
    return -1        

nums = [1,2,3,3,5,8,8,10,10]
target = 1
print(binary_search(nums,target))'''

# Time Complexity: O(log n)
# Space Complexity: O(1)