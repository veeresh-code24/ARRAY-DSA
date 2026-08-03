'''def jos(n,k):
    if n == 1:
        return 0

    return (jos(n-1,k)+k) % n

print(jos(8,3))'''

'''def joseph(n,k):
    if n==1 :
        return 0

    joseph((n-1,k)+k)'''

def per(arr,fi):
    if fi == len(arr) -1:
        print(''.join(arr))
        return


    for i in range(fi, len(arr)):
        arr[fi],arr[i] = arr[i],arr[fi]
        per(arr, fi+1)
        arr[fi],arr[i] = arr[i],arr[fi]

per(['A','B','C'],0)


