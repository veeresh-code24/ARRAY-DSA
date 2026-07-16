#using a two parameter 

'''def fun(arr,l,r):

    if l >= r:
        return
    
    arr[l],arr[r] = arr[r],arr[l]

    fun(arr,l+1,r-1)

def main():
    arr = [1,2,3,4,5]
    n = len(arr)
    fun(arr,0,n-1)
    print(arr)

main()'''


# using a single parameter

def fun(arr,i,n):
    if i > n//2:
        return
    
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]

    fun(arr, i+1,n)

def main():
    arr = [1,2,3,4,5]
    n = len(arr)
    fun(arr,0,n)
    print(arr)

main()