# Brute force

def missing_twice(nums):
    n = len(nums)

    missing = -1
    repeating = -1

    for i in range(1,n+1):
        count = 0
        for j in range(n):
            if nums[j] == i:
                count += 1


        if count == 0:
            missing = i

        elif count == 2:
            repeating = i

    return [repeating, missing]

# nums =  [2, 2]
# nums = [1,3,3]
nums = [4, 3, 6, 2, 1, 1]


print(missing_twice(nums))

# Optimization


def missing_twice(nums):
    n = len(nums)

    i = 0

    while i < n:
        correct = nums[i]-1

        if nums[i] != nums[correct]:
            nums[i],nums[correct] = nums[correct],nums[i]

        else:
            i += 1

    
    for i in range(n):
        if nums[i] != i + 1:
            return [nums[i],i+1]
nums =  [2, 0,2]
# nums = [1,3,3]
# nums = [4, 3, 6, 2, 1, 1]


print(missing_twice(nums))