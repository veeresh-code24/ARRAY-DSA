# Brute Force Approach

def kth_missing_positive(arr,k):
    n = len(arr)

    for i in range(n):
        if arr[i] <= k:
            k += 1
        else:
            break
    return k


# arr = [2,3,4,7,11]
# k = 5
# arr = [1,2,3,4]
# k = 2
arr = [1,2,3,4,5,6,10,11,12]
k = 1
print(kth_missing_positive(arr,k))


# Optimization Approach

def kth_missing_positive(arr,k):
    n = len(arr)

    low,high = 0, n-1

    while low <= high:
        mid = (low+high)//2
        missing = arr[mid] - (mid+1)

        if missing < k:
            low = mid+1

        else:
            high = mid-1
            
# Final k-th missing number calculation
    return k+high+1

arr = [2,3,4,7,11]
k = 5
print(kth_missing_positive(arr,k))


