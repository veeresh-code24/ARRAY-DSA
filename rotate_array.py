# Optimized
'''def rotate_array(nums,k):
    n = len(nums)
    k = k%n
       
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    nums[:] = nums[::-1]
    return nums



nums = [1,2,3,4,5,6,7]
k = 3
print(rotate_array(nums,k))'''

# Better

'''def rotate_array(nums,k):
    n = len(nums)
    k %= n
    temp = nums[0:k]

    for i in range(k,n):
        nums[i-k] = nums[i]

    for i in range(k):
        nums[n-k+i] = temp[i]
    
    return 


nums = [1,2,3,4,5,6,7]
k = 3
print(rotate_array(nums,k))'''


'''def reverse(nums, l, r):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

def rotate_array(nums, k):
    n = len(nums)
    k = k % n

    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)
    reverse(nums, 0, n-1)

    return nums'''

# Right rotate

def left_rotate(nums,k):
    n = len(nums)
    k = k%n
    nums[:] = reversed(nums[::])
    # nums[k:] = reversed(nums[k:])
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    # nums[:] = reversed(nums[::])
    return nums



nums = [1,2,3,4,5,6,7]
k = 3
print(left_rotate(nums,k))