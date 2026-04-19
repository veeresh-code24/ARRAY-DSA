# Brute Force

'''def move_zero(nums):
    n = len(nums)
    arr = []

    for i in range(n):
        if nums[i] != 0:
            arr.append(nums[i])

    for i in range(len(arr)):
        nums[i] = arr[i]
    
    for i in range(len(arr),n):
        nums[i] = 0
    

    return nums

nums = [0,1,0,3,12]
print(move_zero(nums))'''

# Optimization

def move_zero(nums):
    n = len(nums)
    nz = 0
    z = 0

    while nz < n:
        if nums[nz] != 0:
            nums[z],nums[nz] = nums[nz],nums[z]
            nz += 1
            z += 1

        else:
            nz += 1
        
    return nums

nums = [0,1,0,3,12]
print(move_zero(nums))


