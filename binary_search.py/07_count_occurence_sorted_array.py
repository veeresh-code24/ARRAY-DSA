# Brute force

'''def count_occurence_sorted_array(arr,target):
    n = len(arr)
    res = 0

    for i in range(n):
        if arr[i] == target:
            res += 1

    return res

# arr = [0, 0, 1, 1, 1, 2, 3]
# target = 1
arr = [5, 5, 5, 5, 5, 5]
target = 5
print(count_occurence_sorted_array(arr,target))'''

# Optimal Solution

'''def firstOccurence(arr,target):
    n = len(arr)
    low,high = 0 ,n-1
    first = -1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == target:
            first = mid
            high = mid - 1

        elif arr[mid] < target:
            low  = mid+1

        else:
            high = mid-1

    return first

def lastOccurence(arr,target):

    low,high = 0, len(arr)-1
    last = -1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == target:
            last = mid
            low = mid+1

        elif arr[mid] < target:
            low = mid+1

        else:
            high = mid-1

    return last


def first_lastOccurence(arr,target):
    first = firstOccurence(arr,target)
    if first == -1:
        return [-1,-1]
    last = lastOccurence(arr,target)
    return (first,last)

def count(arr,target):

    first,last = first_lastOccurence(arr,target)
    if first == -1:
        return 0
    return last-first+1

arr = [0, 0, 1, 1, 1, 2, 3]
target = 1
# arr = [5, 5, 5, 5, 5, 5]
# target = 5


print(count(arr,target))'''

# Time Complexity: O(2*logN)
# Space Complexity: O(1)