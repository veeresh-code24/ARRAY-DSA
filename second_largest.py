# Brute
'''def second_largest(nums):
    n = len(nums)
    nums.sort()
    largest = nums[-1]

    for i in range(n-1,-1,-1):
        if nums[i] != largest:
            return nums[i]

nums = [8, 8, 7, 6, 5]
print(second_largest(nums))'''


# Better

'''def second_largest(nums):
    largest = second_largest = float('-inf')



    for i in range(len(nums)):
        if nums[i] > largest:
            largest = nums[i]


    for i in range(len(nums)):
        if nums[i] != largest and nums[i] > second_largest:
            second_largest = nums[i]

    return second_largest
    
nums = [-100, -6, -5,-1,-1,12]
print(second_largest(nums))'''

# optimization

def second_largest(nums):

   ''' largest = nums[0]
    second_largest = float('-inf')

    for i in range(1,len(nums)):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]



        else:
            if nums[i] > second_largest and nums[i] != largest:
                second_largest = nums[i]

    return second_largest

nums = [ 6, 5,-1,1,100,12]
print(second_largest(nums))'''





