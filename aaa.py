# def two_sum(nums):
#     n = len(nums)

#     for i in range(n):
#         for j in range(i+1,n):
#             if nums[j] + nums[i] == target:
#                 return i,j

# # nums = [2,7,11,15]
# # target = 9
# nums = [3,3]
# target = 6
# print(two_sum(nums))


# def two_sum(nums):
#     n = len(nums)
#     d = {}

#     for i in range(n):
#         a = nums[i]
#         mpp = target - a

#         if mpp in d:
#             return d[mpp],i
        

#         d[a] = i
#     return d

# # nums = [3,3]
# # nums = [3,2,4]
# # target = 6
# nums = [2,7,11,15]
# target = 9
# print(two_sum(nums))

# def two_sum(nums):
#     n = len(nums)
#     left = 0
#     right = n-1
#     sum = 0

#     while left <= right:
#         sum = nums[left] + nums[right]
#         if sum == target:
#             return "Yes"
        
#         elif sum < target:
#             left += 1
#         else:
#             right -= 1

#     return "False"

# # nums = [2,7,11,15]
# nums = [2,3,5]
# target = 6
# print(two_sum(nums))

# def three_sum(nums):
#     n = len(nums)
#     st = set()

#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     temp = tuple(sorted([nums[i],nums[j],nums[k]]))

            
#             st.add(temp)

#     ans = [list(x) for x in st]
#     return ans

# nums = [-1,0,1,2,-1,-4]
# print(three_sum(nums))


# def three_sum(nums):
#     n = len(nums)
#     st = set()

#     for i in range(n):
#         hashmap = {}
#         for j in range(i+1,n):
#             third = -(nums[i]+nums[j])

#             if third in hashmap:
#                 temp = tuple(sorted([nums[i],nums[j],third]))
#                 st.add(temp)

#             hashmap[nums[j]] = j

#     ans = [list(x) for x in st]
#     return ans

# nums = [-1,0,1,2,-1,-4]
# print(three_sum(nums))


def three_sum(nums):
    nums.sort()
    n = len(nums)
    st = []
    i = 0

    for i in range(n):
        if i >= 0 and nums[i] == nums[i-1]:
            continue

        j = i + 1
        k = n-1

        while j < k:
            total = nums[i]+nums[j]+nums[k]

            if total < 0:
                j += 1
            
            elif total > 0:
                k -= 1

            else:
                st.append([nums[i],nums[j],nums[k]])
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1

    return st


nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))
