# Bruet force

'''def first_last_occurence(nums,target):
    n = len(nums)
    first = -1
    last = -1

    for i in range(n):
        if nums[i] == target:
            if first == -1:
                first = i

            last = i
    return [first,last]


nums = [5,7,7,8,8,10]
target = 8
print(first_last_occurence(nums,target))'''

# Better 

'''def lower_bound(arr, n, x):
    low, high = 0, n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1   # move left
        else:
            low = mid + 1    # move right

    return ans


def upper_bound(arr, n, x):
    low, high = 0, n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > x:
            ans = mid
            high = mid - 1   # move left
        else:
            low = mid + 1    # move right

    return ans


def first_and_last_position(arr, n, k):
    lb = lower_bound(arr, n, k)

    if lb == n or arr[lb] != k:
        return [-1, -1]

    return [lb, upper_bound(arr, n, k) - 1]


# Example
arr = [5, 7, 7, 8, 8, 10]
k = 8
print(first_and_last_position(arr, len(arr), k))'''

# "We can find first and last occurrence using
# lower_bound and upper_bound in O(log n)."

# Optimal Approach

'''def first_last_occurence(nums,target):
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

print(first_last_occurence(nums,target))'''