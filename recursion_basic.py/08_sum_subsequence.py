'''def print_subsequence(i,arr,target,ds,s):
        # Base case

    if i == len(arr):
        if s == target:
            print(ds)

        return
    
    # Take the current element

    ds.append(arr[i])
    s += arr[i]

    print_subsequence(i+1,arr,target,ds,s)
    # Don't take the current element (Backtrack)

    ds.pop()
    s -= arr[i]

    print_subsequence(i+1,arr,target,ds,s)


    
arr = [1,1,1]
target = 2
print_subsequence(0,arr,target,[],0)'''

# STOP early printing one subsequence

'''def print_one_subsequence(ind, arr, ds, s, target):
    # Base case
    if ind == len(arr):
        if s == target:
            print(ds)
            return True
        else:
            return False

    # Pick the current element
    ds.append(arr[ind])
    s += arr[ind]

    if print_one_subsequence(ind + 1, arr, ds, s, target):
        return True

    # Backtrack
    s -= arr[ind]
    ds.pop()

    # Not pick the current element
    if print_one_subsequence(ind + 1, arr, ds, s, target):
        return True

    return False


# Driver code
arr = [1, 2, 1]
target = 2

# print_one_subsequence(0, arr, [], 0, target)

'''

# Count Subsequence

def count_subsequence(ind, arr, curr_sum, target):
    # Base case
    if ind == len(arr):
        if curr_sum == target:
            return 1
        else:
            return 0

    # Pick the current element
    curr_sum += arr[ind]
    left = count_subsequence(ind + 1, arr, curr_sum, target)

    # Backtrack
    curr_sum -= arr[ind]

    # Don't pick the current element
    right = count_subsequence(ind + 1, arr, curr_sum, target)

    # Total count
    return left + right


# Driver code
arr = [1, 2, 1]
target = 2

print(count_subsequence(0, arr, 0, target))

# Count The subSequence

def print_sub_sequence(ind,arr,target,sum):
    if ind == len(arr):
        if sum  == target:
            return 1

        else:
            return 0
         
    
    # Pick the current element

    sum += arr[ind]

    left = print_sub_sequence(ind+1,arr,target,sum)

    sum -= arr[ind]

    right = print_sub_sequence(ind+1,arr,target,sum)


    return left + right

arr = [1,2,1]
target = 2
count = 0
print(print_sub_sequence(0,arr,target,0))
