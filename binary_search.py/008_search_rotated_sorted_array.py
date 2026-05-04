# Bruet Force

def sorted_rotated_arrayll(nums,target):

    for i in range(len(nums)):
        if nums[i] == target:
            return True
        
    return False

# nums = [2,5,6,0,0,1,2]
# target = 0
nums = [2,5,6,0,0,1,2]
target = 3
print(sorted_rotated_arrayll(nums,target))

# Optimal

def sorted_rotated_arrayll(nums,target):

        low,high = 0,len(nums)-1

        while low <= high:
            mid = (low+high)//2

            if nums[mid] == target:
                return True

            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue


            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1

            else:
                if nums[mid] < target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1

        return False


# nums = [2,5,6,0,0,1,2]
# target = 0
nums = [2,5,6,0,0,1,2]
target = 3
print(sorted_rotated_arrayll(nums,target))



