# Brute Force

def Kth_element_sorted(a,b,k):
    n = len(a)
    m = len(b)

    i,j=0,0
    arr = []

    while i < n and j < m:
        if a[i] <= b[j]:
            arr.append(a[i])
            i += 1

        else:
            arr.append(b[j])
            j += 1

    while i < n:
        arr.append(a[i])
        i += 1

    while j < m:
        arr.append(b[j])
        j += 1

    return arr[k-1]

# a = [2, 3, 6, 7, 9]
# b = [1, 4, 8, 10]
# k = 5
a = [100, 112, 256, 349, 770]
b = [72, 86, 113, 119, 265, 445, 892]
k = 7
print(Kth_element_sorted(a,b,k))
