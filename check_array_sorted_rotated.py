# Array is sorted or rotated

'''def arr_sorted_rotated(nums):
    n = len(nums)
    count = 0

    for i in range(n):
        if nums[i] > nums[(i+1)%n]:
            count += 1


    return count <= 1


nums = [2,1,3,4]
print(arr_sorted_rotated(nums))'''


# array is sorted

def arr_sorted_rotated(nums):
    n = len(nums)


    for i in range(1,n):
        if nums[i] < nums[i-1]:
            return False

    return True

# nums = [2,1,3,4]
nums = [1,2,3,4]
print(arr_sorted_rotated(nums))