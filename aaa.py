# def upper_bound(nums,x):
#     ans = len(nums)
#     for i in range(len(nums)):
#         if nums[i] > x:
#             ans = i
#             break

#     return ans

# # nums = [1,2,2,3]
# # x = 2
# nums = [3,5,8,15,19]
# x = 9
# print(upper_bound(nums,x))

# def insert_position(nums,x):
#     ans = len(nums)

#     low,high = 0, len(nums)-1

#     while low <= high:
#         mid = (low+high)//2

#         if nums[mid] >= x:
#             ans = mid
#             high = mid-1

#         else:
#             low = mid+1

#     return ans

# # nums = [1,2,2,3]
# # x = 2
# # nums = [3,5,8,15,19]
# # x = 9
# nums = [1,3,5,6]
# x = 7

# print(insert_position(nums,x))

# def floor(nums,x):

#     ans = -1

#     low,high =0,len(nums)-1

#     while low <= high:
#         mid = (low+high)//2

#         if nums[mid] <= x:
#             ans = nums[mid]
#             low = mid+1

#         else:
#             high = mid-1

#     return ans

# def ceil(nums,x):

#     ans = -1

#     low,high = 0, len(nums)-1

#     while low <= high:
#         mid = (low+high)//2

#         if nums[mid] >= x:
#             ans = nums[mid]
#             high = mid-1

#         else:
#             low = mid+1

#     return ans





# nums =[2,4,6,8,10,12,14]
# x= 1
# print(floor(nums,x))
# print(ceil(nums,x))

# def first(nums,target):
#     n = len(nums)

#     low,high = 0,n-1
#     res = [-1,-1]

#     while low <= high:
#         mid = (low+high)//2

#         if nums[mid] == target:
#             res[0] = mid
#             high = mid-1

#         elif nums[mid] < target:
#             low = mid+1

#         else:
#             high = mid-1


#     low,high = 0,n-1

#     while low <= high:
#         mid= (low+high)//2

#         if nums[mid] == target:
#             res[1] = mid
#             low = mid+1

#         elif nums[mid] < target:
#             low = mid+1

#         else:
#             high = mid-1

#     return res

# nums = [5,7,7,8,8,10]
# target = 6
# print(first(nums,target))


'''def firstOccurence(arr,target):
    n = len(arr)

    first = -1
    low,high = 0,n-1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == target:
            first = mid
            high = mid-1

        elif  arr[mid] < target:
            low = mid+1

        else:
            high = mid-1

    return first

def last_occurence(arr,target):
    n = len(arr) 
    low,high = 0, n-1
    last = -1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == target:
            last = mid
            low = mid+1

        elif arr[mid] < target:
            low = mid+1

        else:
            high = mid-1

    return last

def firstLastOccurence(arr,target):
    first = firstOccurence(arr,target)
    if first == -1:
        return [-1,-1]
    
    last =  last_occurence(arr,target)
    return [first,last]

def count(arr,target):
    first,last = firstLastOccurence(arr,target)
    if first == -1:
        return 0
    return (last-first+1)

# arr = [0, 0, 1, 1, 1, 2, 3]
# target = 1
arr = [5, 5, 5, 5, 5, 5]
target = 5
print(count(arr,target))'''


# def search_rotate_sorted(nums,target):
#     n = len(nums)

#     low,high = 0,n-1

#     while low <= high:
#         mid = (low+high)//2

#         if nums[mid] == target:
#             return mid
        
#         elif nums[low] <= nums[mid]:
#             if nums[low] <= target < nums[mid]:
#                 high = mid-1
#             else:
#                 low = mid+1

#         else:
#             if nums[mid] < target <= nums[high]:
#                 low = mid+1
#             else:
#                 high  = mid-1

#     return -1
            
# nums = [4,5,6,7,0,1,2]
# target = 0
# print(search_rotate_sorted(nums,target))


def how_many_rotated(nums):
    n = len(nums)

    low,high = 0,n-1

    while low < high:
        mid = (low+high)//2

        if nums[mid] > nums[high]:
            low = mid+1
            
        else:
            high = mid


    return low




# nums = [3,4,5,1,2]
nums = [1,2]

print(how_many_rotated(nums))








