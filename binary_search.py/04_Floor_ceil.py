# Brute Force

def floor_linear(nums,x):
    ans = 0

    for i in range(len(nums)):
        if nums[i] <= x:
            ans = nums[i]

    return ans
def ceil_linear(nums,x):
    ans = -1


    for i in range(len(nums)):
        if nums[i] >= x:
            ans = nums[i]
            break

    return ans

nums =[3, 4, 4, 7, 8, 10]
x= 6
print("Floor: ", floor_linear(nums,x))
print("Ceil: ",ceil_linear(nums,x))
#   Optimal Opproach


'''def floor(nums,x):
    low,high = 0,len(nums)-1
    ans = -1

    while low <= high:
        mid = (low+high)//2

        if nums[mid] <= x:
            ans = nums[mid]
            low = mid+1

        else:
            high = mid-1

    return ans

def ceil(nums,x):
    low,high = 0,len(nums)-1
    ans = -1

    while low <= high:
        mid = (low+high)//2

        if nums[mid] >= x:
            ans = nums[mid]
            high = mid-1

        else:
            low = mid+1

    return ans

nums =[3, 4, 4, 7, 8, 10]
x= 8
print("Floor: ", floor(nums,x))
print("Ceil: ",ceil(nums,x))'''

# optimization 2

def floor_ceil(nums, x):
    low, high = 0, len(nums) - 1
    floor_val = -1
    ceil_val = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == x:
            return nums[mid], nums[mid]

        elif nums[mid] < x:
            floor_val = nums[mid]   # possible floor
            low = mid + 1

        else:
            ceil_val = nums[mid]    # possible ceil
            high = mid - 1

    return [floor_val, ceil_val]

nums = [2,4,6,8,10,12,14]
x = 5

print(floor_ceil(nums, x))