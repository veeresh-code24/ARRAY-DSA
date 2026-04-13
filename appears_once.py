# Brute
'''def appers_ones(nums):
    n = len(nums)

    for i in range(n):
        num = nums[i]
        count = 0
        for j in range(n):
            if nums[j] == num:
                count += 1


        if count == 1:
            return num
            

    return -1

nums = [1,2,1,2,3,4,3,3,5,4]
print(appers_ones(nums))'''

# Better

'''def appers_ones(nums):
    n = len(nums)
    d ={}

    for i in range(n):
        if nums[i] not in d:
            d[nums[i]] = 1
        else:
            d[nums[i]] += 1

    for key,value in d.items():
        if value == 1:
            return key
nums = [1,2,1,2,3,4,3,3,5,4]
print(appers_ones(nums))'''


# Optimization

def appers_ones(nums):
    n = len(nums)
    xorr = 0

    for i in range(n):
        xorr ^= nums[i]
    return xorr







nums = [1,2,1,2,3,3,6]
print(appers_ones(nums))


