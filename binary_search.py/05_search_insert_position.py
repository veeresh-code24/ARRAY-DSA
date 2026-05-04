# Brute Approach

'''def search_insert_posi(nums,target):
    n = len(nums)

    for i in range(n):
        if nums[i] >= target:
            return i

    
nums = [1,3,5,6]
target = 2
print(search_insert_posi(nums,target))'''


# Optimal Approach

def search_insert_posi(nums,target):
    low,high = 0,len(nums)-1
    ans = len(nums)

    while low <= high:
        mid = (low+high)//2

        if nums[mid] >= target:
            ans = mid
            high = mid-1

        else:
            low = mid+1

    return ans

nums = [1,3,5,6]
target = 7
print(search_insert_posi(nums,target))

# Time → O(log n)
# Space → O(1)

