

def first_last_occurence(nums,target):
    n = len(nums)

    low,high = 0,n-1
    res = [-1,-1]

    while low <= high:
        mid = (low+high)//2

        if nums[mid] == target:
            res[0] = mid
            high = mid-1


        elif nums[mid] < target:
            low = mid+1


        else:
            high = mid-1

    low,high = 0,n-1

    while low <= high:
        mid = (low+high)//2

        if nums[mid] == target:
            res[1] = mid
            low = mid+1

        elif nums[mid] < target:
            low = mid+1

        else:
            high = mid-1

    return res


# nums = [5,7,7,8,8,10]
# target = 8
nums = []
target = 0

print(first_last_occurence(nums,target))