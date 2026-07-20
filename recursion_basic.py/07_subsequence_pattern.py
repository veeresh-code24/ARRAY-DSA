'''def print_subsequence(ind, arr, ds, n):
    if ind == n:
        if len(ds) == 0:
            print("[]")
        else:
            print(*ds)
        return
    
        # Pick the current element

    ds.append(arr[ind])
    print_subsequence(ind+1, arr, ds, n)

    # Backtrack

    ds.pop()

    # Not pick the current element

    print_subsequence(ind+1, arr, ds, n)


def main():
    arr = [3,1,2]
    n = len(arr)
    ds = []
    print_subsequence(0, arr, ds, n)

main()'''


# PRINTING IN REVERSE ORDER

'''def print_subsequence(ind, ds, arr, n):
    if ind == n:
        if len(ds) == 0:
            print("{}")
        else:
            print(*ds)
        return

    # Don't pick first
    print_subsequence(ind + 1, ds, arr, n)

    # Pick later
    ds.append(arr[ind])
    print_subsequence(ind + 1, ds, arr, n)
    ds.pop()


arr = [3, 1, 2]
print_subsequence(0, [], arr, len(arr))
'''
