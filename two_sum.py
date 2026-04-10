# Brute force

'''def two_sum(nums,target):
    n = len(nums)

    for i in range(n):
        for j in range(i+1,n):
            if nums[j] + nums[i] == target:
                return i,j
            

nums = [1, 3, 5, -7, 6, -3]
target = 0
print(two_sum(nums,target))'''


# optimal for pair return

'''def two_sum(nums,target):
    n = len(nums)
    d = {}

    for i in range(n):
        a = nums[i]
        mpp = target - a
        if mpp in d:
            return d[mpp],i
        
        d[a] = i

nums = [1, 6, 2, 10, 3]
target = 7
print(two_sum(nums,target))'''


# optimal YES or 


def two_sum(nums,target):
    n = len(nums)
    nums.sort()
    left = 0
    right = n-1

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            return "Yes"
        
        if sum < target:
            left += 1
        else:
            right -= 1

    return "False"

nums = [1, 6, 2, 10, 3]
target = 7
print(two_sum(nums,target))
        











