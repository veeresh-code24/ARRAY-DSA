# Subsequence 

# Pick and Not pick

'''def subsequence(ind, arr, ds, n):
    if ind == n:
        print(ds)
        return

    ds.append(arr[ind])
    subsequence(ind + 1, arr, ds, n)

    ds.pop()
    subsequence(ind+1, arr, ds, n)


arr = [0,1,2]
n = len(arr)
subsequence(0, arr, [], n)'''

# Not Pick and Pick

def subsequence(ind, arr, ds, n):
    if ind == n:
        print(ds)
        return 


    subsequence(ind+1, arr, ds, n)

    ds.append(arr[ind])
    subsequence(ind+1, arr, ds, n)

    ds.pop()


arr = [3,1,2]
n = len(arr)
subsequence(0, arr, [], n)



