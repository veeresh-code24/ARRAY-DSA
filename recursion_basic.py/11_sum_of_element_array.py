def sum_arr(arr,i):
    if i >= len(arr):
        return 0

    return arr[i] + sum_arr(arr,i+1)

arr = [1,2,3,4,5]
print(sum_arr(arr,0))