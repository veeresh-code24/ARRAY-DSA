def count_student(arr,pages):
    n = len(arr)
    student = 1
    pages_student = 0
    for i in range(n):
        if pages_student + arr[i] <= pages:
            pages_student += arr[i]

        else:
            student += 1
            pages_student = arr[i]

    return student



def findPages(arr,n,m):
    if m > n:
        return -1
    
    low = max(arr)
    high = sum(arr)

    for pages in range(low,high+1):
        if count_student(arr,pages) == m:
            return pages

    return low

arr = [12, 34, 67, 90]
n = 4
m = 2

print(findPages(arr,n,m))


# Time Complexity: O(N * (sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[])
# Space Complexity:  O(1)

def count_student(arr,pages):
    n  = len(arr)
    student = 1
    pagesStudent = 0

    for i in range(n):
        if pagesStudent + arr[i] <= pages:
            pagesStudent += arr[i]

        else:
            student += 1
            pagesStudent = arr[i]

    return student

def findPages(arr,n,m):

    if m > n:
        return -1
    
    low = max(arr)
    high = sum(arr)

    while low <= high:
        mid = (low+high)//2

        students = count_student(arr,mid)

        if students > m:
            low = mid+1

        else:
            high = mid-1

    return low

arr = [25, 46, 28, 49, 24]
n = 5
m = 4
print(findPages(arr,n,m))



