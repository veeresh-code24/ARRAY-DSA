def permutation(ar,fi):
    if  (fi == len(ar)-1):
        print("".join(ar))
        return

    for i in range(fi, len(ar)):
        ar[fi],ar[i] = ar[i],ar[fi]
        permutation(ar,fi+1)
        ar[fi],ar[i] = ar[i],ar[fi]


permutation(['A','B','C','D'],0)




