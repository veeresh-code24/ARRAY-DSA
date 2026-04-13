# Brute force

'''def sort_clors(nums):

    nums.sort()

    return nums


nums = [2,0,2,1,1,0]
print(sort_clors(nums))'''

# Better


'''def sort_clors(nums):
    n = len(nums)
    count0,count1,count2 = 0,0,0


    for i in range(n):
        if nums[i] == 0:
            count0 += 1


        elif nums[i] == 1:
            count1 += 1

        else:
            count2 += 1

    for i in range(count0):
        nums[i] = 0

    for i in range(count0,count0+count1):
        nums[i] = 1

    for i in range(count0+count1,len(nums)):
        nums[i] = 2

    return nums

nums = [2,0,2,1,1,0]
print(sort_clors(nums))'''

# Brute

'''def sort_clors(nums):
    n = len(nums)

    low,mid,high = 0,0,n-1

    while mid <= high:
        if nums[mid] == 0:
            nums[low],nums[mid] = nums[mid],nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:
            nums[mid],nums[high] = nums[high],nums[mid]
            high -= 1

    return nums




nums = [2,0,2,1,1,0]
print(sort_clors(nums))'''




