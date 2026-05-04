# Brute

'''def lower_bound(nums,x):
    n = len(nums)

    for i in range(n):
        if nums[i] >= x:
            return i
    
    return n
        

nums= [1,2,2,3]
x = 2
nums= [3,5,8,15,19]
x = 9
nums= [3,5,8,15,19]
x = 20
print(lower_bound(nums,x))'''

# Optimal Approach

'''def lower_bound(nums,x):
    n = len(nums)

    low, high = 0,n-1
    ans = n

    while low <= high:
        mid = (low+high)//2

        if nums[mid] >= x:
            ans = mid
            high = mid-1
        
        else:
            low = mid+1

    return ans

# nums= [1,2,2,3]
# x = 2
# nums= [3,5,8,15,19]
# x = 9
nums= [3,5,8,15,19]
x = 20
print(lower_bound(nums,x))'''

# Time Complexity: O(log n)
# Space Complexity: O(1)