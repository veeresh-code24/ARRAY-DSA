def count_subset(arr,sum,i):
    if sum == 0:
        return 1

    if sum < 0:
        return 0

    if i == len(arr):
        return 0

    return count_subset(arr, sum - arr[i], i+1) + count_subset(arr, sum,i+1)





arr = [10,15,25,5]
print(count_subset(arr,25,0))