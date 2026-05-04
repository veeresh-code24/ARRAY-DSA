# Brute Force

'''def upper_bound(nums,x):

    for i in range(n):
        if nums[i] > x:
            return i
        
    return n

# n= 4
# nums = [1,2,2,3]
# x = 2
n = 5
nums = [3,5,8,15,19]
x = 3
print(upper_bound(nums,x))'''

# TC ---  O(N)
# SC ----- O(1)

# Optimal Approach

def upper_bound(nums,x):
    low,high = 0,len(nums)-1
    ans = len(nums)

    while low <= high:
        mid = (low+high)//2

        if nums[mid] > x:
            ans = mid
            high = mid-1

        else:
            low = mid+1

    return ans


# nums = [1,2,2,3]
# x = 4
nums = [3,5,8,15,19]
x = 14
print(upper_bound(nums,x))

# Optimal → O(log n)
# Space → O(1)






