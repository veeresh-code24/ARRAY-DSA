def inversion_count(arr):
    n = len(arr)

    # if 
    # res = []
    count = 0

    for i in range(n):
        # count = 0
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                # res.append([arr[i],arr[j]])
                count += 1

    return count

arr = [2, 4, 1, 3, 5]
# arr = [2, 3, 4, 5, 6]
# arr  = [10,10,10]


print(inversion_count(arr))
