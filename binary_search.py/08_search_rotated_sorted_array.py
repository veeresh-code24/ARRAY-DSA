# Bruet Force

'''def search_rotated_sor_arr(nums,target):
    n = len(nums)

    for i in range(n):
        if nums[i] == target:
            return i
        
    return -1

# nums = [4,5,6,7,0,1,2]
# target = 0
# nums = [4,5,6,7,0,1,2]
# target = 3
nums = [1]
target = 0
print(search_rotated_sor_arr(nums,target))'''

# Optimal Solution

def search_rotated_sor_arr(nums,target):
    n = len(nums)

    low,high = 0, n-1

    while low <= high:
        mid = (low+high)//2

        if nums[mid] == target:
            return True
        
         # Check if left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid -1
            else:
                low = mid+1

         # Right half is sorted
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid+1
            else:
                high = mid-1

    return False
              
nums = [4,5,6,7,0,1,2]
target = 8
print(search_rotated_sor_arr(nums,target))