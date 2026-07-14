# Brute force

'''def largest_element(nums):
    nums.sort()
    return nums[-1]

nums = [3,3,6,1]
print(largest_element(nums))'''

# optimal

'''def largest_element(nums):
    n = len(nums)
    largest = nums[0]

    for i in range(1,n):
        if nums[i] > largest:
            largest = nums[i]

    return largest

# nums = [3,3,6,1]
nums = [8, 10, 5, 7, 9]
print(largest_element(nums))'''

# def second_largest(nums):

#     largest = nums[-1]

#     for i in range(len(nums)-1,-1,-1):
#         if nums[i] != largest:
#             return nums[i]


# nums = [21,34,1,2,4,53,100]
# print(second_largest(nums))




def second_largest(nums):

    first_lar = -1
    second_lar = -1

    for i in range(len(nums)):
        if nums[i] > first_lar:
            second_lar = first_lar
            first_lar = nums[i]



        elif nums[i] < first_lar and nums[i] > second_lar:
            second_lar = nums[i]


    return second_lar

        
nums = [21,34,1,2,4,53,100]
print(second_largest(nums))


