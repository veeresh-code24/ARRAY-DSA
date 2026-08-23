# Pick Not Pick Pattern


'''def print_suubsequence_sum_k(ind, arr, ds,s, target, n):
    if ind == n:
        if s == target:
            print(ds)
        return
    
    # TAKE
    ds.append(arr[ind])
    s += arr[ind]
    print_suubsequence_sum_k(ind+1, arr, ds,s, target, n)

    # UNDO
    s -= arr[ind]
    ds.pop()

    # NOT TAKE
    print_suubsequence_sum_k(ind+1, arr, ds,s, target, n)


arr = [1,2,1]
n = len(arr)
target = 2
print_suubsequence_sum_k(0, arr, [],0, target, n)'''


# Print First subsequence

'''def print_fir_subseq_equal_target(ind, arr, ds,s, target, n):

    if ind == n:
        if s == target:
            print(ds)
            return True
        return False

    ds.append(arr[ind])
    s += arr[ind]

    if print_fir_subseq_equal_target(ind+1, arr, ds,s, target, n):
        return True

    s -= arr[ind]
    ds.pop()

    if print_fir_subseq_equal_target(ind+1, arr, ds,s, target, n):
        return True


    return False


arr = [1,2,1]
target = 2
n = len(arr)
print_fir_subseq_equal_target(0, arr, [],0, target, n) '''

# Print Total Count subsequence 

def print_fir_subseq_equal_target(ind, arr,s, target, n):

    if ind == n:
        if s == target:
            return 1
        return 0

    # TAKE
    take = print_fir_subseq_equal_target(ind+1,arr,s+arr[ind], target, n)

    # NOT TAKE
    not_take = print_fir_subseq_equal_target(ind+1, arr,s, target, n)


    # Add both answers and return
    return take + not_take


arr = [1,2,1]
target = 2
n = len(arr)
print(print_fir_subseq_equal_target(0, arr,0, target, n))

