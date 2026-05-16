'''def lower_bound(nums,x):
    n = len(nums)

    for i in range(n):
        if nums[i] >= x:
            return i


nums= [1,2,2,3]
x = 2
# nums= [3,5,8,15,19]
# x = 9
print(lower_bound(nums,x))




def lower_bound(nums,x):
    n = len(nums)
    low,high= 0, n-1
    ans = -1

    while low <= high:
        mid = (low+high)//2

        if nums[mid] >= x:
            ans = mid
            high = mid-1

        else:
            low = mid+1

    return low


# nums= [1,2,2,3]
# x = 2
nums= [3,5,8,15,19]
x = 9
print(lower_bound(nums,x))'''

'''def upper_bound(nums,x,n):

    for i in range(n):
        if nums[i] > x:
            return i

# n= 4
# nums = [1,2,2,3]
# x = 2
n = 5
nums = [3,5,8,15,19]
x = 9
print(upper_bound(nums,x,n))

def upper_bound(nums,x,n):

    low,high = 0,n-1

    while low <= high:
        mid = (low+high)//2

        if nums[mid] > x:
            high = mid-1

        else:
            low = mid+1

    return low

n= 4
# nums = [1,2,2,3]
# x = 2
n = 5
nums = [3,5,8,15,19]
x = 9
print(upper_bound(nums,x,n))'''

'''def search_insert(nums,target):
    n = len(nums)

    for i in range(n):
        if nums[i] >= target:
            return i


nums = [1, 3, 5, 6]
target = 2
print(search_insert(nums,target))

def search_insert(nums,target):
    n = len(nums)
    low,high = 0,n-1

    while low <= high:
        mid = (low+high)//2

        if nums[mid] >= target:
            high = mid-1

        else:
            low = mid+1

    return low

nums = [1, 3, 5, 6]
target = 2
print(search_insert(nums,target))'''


'''def florr(nums,x):
    n = len(nums)
    ans = -1

    for i in range(n):
        if nums[i] <= x:
            ans = nums[i]
        
        else:
            break

    return ans

def ceil(nums,x):
    n = len(nums)
    ans = -1

    for i in range(n):
        if nums[i] >= x:
            return nums[i]
        
nums =[3, 4, 4, 7, 8, 10]
x= 8  
print(florr(nums,x))
print(ceil(nums,x))

def floor(nums,x):
    n = len(nums)
    ans = -1

    low,high = 0,n-1

    while low <= high:
        mid = (low+high)//2

        if nums[mid] <= x:
            ans = nums[mid]
            low = mid+1

        else:
            high = mid-1

    return ans

def ceil(nums,x):
    n = len(nums)
    ans = -1

    low,high = 0,n-1

    while low <= high:
        mid = (low+high)//2

        if nums[mid] >= x:
            ans = nums[mid]
            high = mid-1

        else:
            low = mid+1

    return ans

nums =[3, 4, 4, 7, 8, 10]
x= 5
print(floor(nums,x))
print(ceil(nums,x))'''

'''def firstOccurence(nums,target):
    n = len(nums)

    low,high = 0,n-1
    res = [-1,-1]

    while low <= high:
        mid = (low+high)//2

        if nums[mid] == target:
            res[0] = mid
            high = mid-1

        elif nums[mid] < target:
            low = mid+1

        else:
            high = mid-1

    if res[0] == -1:
        return res
    

    low,high = 0,n-1
    while low <= high:
        mid = (low+high)//2

        if nums[mid] == target:
            res[1] = mid
            low = mid+1

        elif nums[mid] < target:
            low = mid+1

        else:
            high = mid-1

    return res

nums = [5,7,7,8,8,10]
target = 6
print(firstOccurence(nums,target))'''

'''def firstlastOccurence(nums,target):
    n = len(nums)
    first = -1
    last = -1

    for i in range(n):
        if nums[i] == target:
            if first == -1:
                first = i

            last = i

    return [first,last]

nums = [5,7,7,8,8,10]
target = 8
print(firstlastOccurence(nums,target))'''

'''def firstOccurence(nums,target):
    n = len(nums)

    low,high = 0,n-1
    first = -1

    while low <= high:
        mid = (low+high)//2

        if nums[mid] == target:
            first = mid
            high = mid-1

        elif nums[mid] < target:
            low = mid+1

        else:
            high = mid-1

    return first

def lastOccurence(nums,target):
    n = len(nums)
    last = -1   

    low,high = 0,n-1
    while low <= high:
        mid = (low+high)//2

        if nums[mid] == target:
            last = mid
            low = mid+1

        elif nums[mid] < target:
            low = mid+1

        else:
            high = mid-1

    return last

def FirstLastOccurence(nums,target):
    first = firstOccurence(nums,target)
    if first == -1:
        return [-1,-1]
    last = lastOccurence(nums,target)
    return (first,last)

def count(nums,target):
    first,last = FirstLastOccurence(nums,target)
    if first == -1:
        return 0
    
    return last-first+1



# nums = [0, 0, 1, 1, 1, 2, 3]
# target = 1
nums= [5, 5, 5, 5, 5, 5]
target = 5
print(count(nums,target))'''

'''def searchRotatedSorted(nums,target):
    n = len(nums)

    for i in range(n):
        if nums[i] == target:
            return i
        
    return -1

nums = [4,5,6,7,0,1,2]
target = 3
print(searchRotatedSorted(nums,target))   

def searchRotatedSorted(nums,target):
    n = len(nums)

    low,high = 0, n-1

    while low <= high:
        mid = (low+high)//2

        if nums[mid] == target:
            return True
        
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
        
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid-1

            else:
                low = mid+1

        else:
            if nums[mid] < target <= nums[high]:
                low = mid+1

            else:
                high = mid-1

    return False

# nums = [4,5,6,7,0,1,2]
# target = 2
nums = [2,5,6,0,0,1,2]
target = 3
print(searchRotatedSorted(nums,target)) '''

def Kth_element_sorted(a,b,k):
    n = len(a)
    m = len(b)
    i= 0 
    j = 0
    arr = []
    while i < n and j <m:
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

    for i in range(len(arr)):
        if i == k-1:
            return arr[i]

a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
print(Kth_element_sorted(a,b,k))


    







        









