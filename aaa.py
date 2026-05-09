'''def single_element(nums):
    n = len(nums)

    if n == 1:
        return nums[0]
    
    if nums[0] != nums[1]:
        return nums[0]
    
    if nums[n-1] != nums[n-2]:
        return nums[n-1]
    
    low,high = 1, n-2

    while low <= high:
        mid = (low+high)//2

        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]
        
        if ((mid%2== 1 and nums[mid-1] == nums[mid]) or
            (mid%2==0 and nums[mid] == nums[mid+1])):
            low = mid+1

        else:
            high = mid-1

    return -1

    

# nums = [1,1,2,2,3,4,4,5,5]
nums = [1,2,3]
print(single_element(nums))

# print("irannna")'''


'''def find_peak_element(nums):
    n = len(nums)

    if n ==1:
        return nums[0]
    
    if nums[0] > nums[1]:
        return nums[0]
    
    if nums[n-1] > nums[n-2]:
        return nums[n-1]
    
    low,high = 1,n-2

    while low <= high:
        mid= (low+high)//2

        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return nums[mid]
        
        if nums[mid] > nums[mid-1]:
            low = mid+1

        else:
            high = mid-1

    return -1
    



# nums = [1,2,3,1]
# nums = [1,2,1,3,5,6,4]
nums = [1,2,3,4,5,10,1]
print(find_peak_element(nums))'''

# def square_root(n):
#     ans = 1
#     for i in range(1,n):
#         if i * i <= n:
#             ans = i
#     return ans
    
# n = 80
# print(square_root(n))

# def square_root(n):
#     low,high=0, n-1
#     ans = 1

#     while low <= high:
#         mid = (low+high)//2

#         if mid* mid <= n:
#             ans = mid
#             low = mid+1

#         else:
#             high = mid-1

#     return ans


# n = 47
# print(square_root(n))

def nth_root(n,m):

    for i in range(1,m):
        if i ** n == m:
            return i
        
    return -1

n = 4
m = 69
print(nth_root(n,m))


def nthroot_number(n,m):

    low,high = 1, m

    while low <= high:
        mid = (low+high)//2

        if (mid**n)==m:
            return mid
        
        elif (mid**n) < m:
            low = mid+1
        else:
            high = mid-1

    return -1
n = 2
m = 16
print(nthroot_number(n,m))

