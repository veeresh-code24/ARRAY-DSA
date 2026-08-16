# Brute Force

def no_of_gre_right(arr, indices):
    n = len(arr)
    stack = []

    for index in indices:
        count = 0
        for j in range(index+1, n):
            if arr[j] > arr[index]:
                count += 1

        stack.append(count)

    return stack


# arr = [3, 4, 2, 7, 5, 8, 10, 6]
# indices = [0, 5]
arr = [1, 2, 3, 4, 1]
indices = [0, 3]
print(no_of_gre_right(arr, indices))