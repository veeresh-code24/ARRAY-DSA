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

def first(nums,target):
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


    low,high = 0,n-1

    while low <= high:
        mid= (low+high)//2

        if nums[mid] == target:
            res[1] = mid
            low = mid+1

        elif nums[mid] < target:
            low = mid+1

        else:
            high = mid-1

    return res

nums = []
target = 6
print(first(nums,target))