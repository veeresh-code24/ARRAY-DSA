# def three_sum(nums):
#     n = len(nums)
#     st = set()

#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     temp = tuple(sorted([nums[i],nums[j],nums[k]]))
#                     st.add(temp)

#     return [list(x) for x in st]


# nums = [-1,0,1,2,-1,-4]
# print(three_sum(nums))

# def three_sum(nums):
#     n = len(nums)
#     st = set()
     

#     for i in range(n):
#         hashset = set()

#         for j in range(i+1,n):
#             target = -(nums[i]+nums[j])

#             if target in hashset:
#                 temp = tuple(sorted([nums[i],nums[j],target]))
#                 st.add(temp)

#             hashset.add(nums[j])

#     return [list(x) for x in st]


# nums = [-1,0,1,2,-1,-4]
# print(three_sum(nums))


# def three_sum(nums):
#     n = len(nums)
#     nums.sort()
#     arr = []

#     for i in range(n):
#         if i > 0 and nums[i] == nums[i-1]:
#             continue

#         j = i + 1
#         k = n-1

#         while j < k:
#             target = nums[i]+nums[j]+nums[k]
#             if target < 0:
#                 j += 1

#             elif target > 0:
#                 k -= 1

#             else:
#                 arr.append([nums[i],nums[j],nums[k]])
#                 j += 1
#                 k -= 1

#                 while j < k and nums[j] == nums[j-1]:
#                     j += 1
#                 while j < k and nums[k] == nums[k+1]:
#                     k -= 1


#     return arr


# nums = [0,0,0]
# print(three_sum(nums))

# def four_sum(nums,target):
#     n = len(nums)
#     st = set()

#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 for z in range(k+1,n):
#                     if nums[i] + nums[j] + nums[k] + nums[z] == target:
#                         temp = tuple(sorted([nums[i],nums[j],nums[k],nums[z]]))
#                         st.add(temp)

#     return [list(x) for x in st]


# # nums = [1,0,-1,0,-2,2]
# nums = [2,2,2,2]
# target = 8
# print(four_sum(nums,target))


# def four_sum(nums,target):
#     n = len(nums)
#     st = set()

#     for i in range(n):
#         for j in range(i+1,n):
#             hashset = set()
#             for k in  range(j+1,n):
#                 fourth = target-(nums[i]+nums[j]+nums[k])
#                 if fourth in hashset:
#                     temp = tuple(sorted([nums[i],nums[j],nums[k],fourth]))
#                     st.add(temp)

#                 hashset.add(nums[k])

#     return [list(x) for x in st]
                
# # nums = [1,0,-1,0,-2,2]
# nums = [2,2,2,2]
# target = 8
# print(four_sum(nums,target))

# def four_sum(nums,target):
#     n = len(nums)
#     nums.sort()
#     arr = []

#     for i in range(n):
#         if i > 0 and nums[i] == nums[i-1]:
#             continue

#         # j = i +1
#         for j in range(i+1,n):
#             if j > i+1 and nums[j] == nums[j-1]:
#                 continue

#             k = j +1
#             z = n-1

#             while k < z:
#                 total = nums[i]+nums[j]+nums[k]+nums[z]

#                 if total == target:
#                     arr.append([nums[i],nums[j],nums[k],nums[z]])
#                     k += 1
#                     z -= 1

#                     while k < z and nums[k] == nums[k-1]:
#                         k += 1

#                     while k < z and nums[z] == nums[z+1]:
#                         z -= 1

#                 elif total < target:
#                     k += 1
#                 else:
#                     z -= 1

#     return arr

                
# # nums = [1,0,-1,0,-2,2]
# nums = [2,2,2,2]
# target = 8
# print(four_sum(nums,target))

# def longest_subarray(nums,k):
#     n = len(nums)
#     max_len = 0


#     for i in range(n):
#         pre_sum = 0
#         for j in range(i,n):
                
#             pre_sum = 0
#             for x in range(i,j+1):
#                 pre_sum += nums[x]


#             if pre_sum == k:
#                 max_len = max(max_len,j-i+1)

#     return max_len



# nums = [10, 5, 2, 7, 1, 9]
# k=15
# print(longest_subarray(nums,k))


# def longest_subarray(nums,k):
#     n = len(nums)
#     hash = {0:-1}
#     max_len = 0
#     pre_sum = 0


#     for i in range(n):
#         pre_sum += nums[i]

#         if pre_sum - k in hash:

#             lenght = i-hash[pre_sum-k]
#             max_len = max(max_len,lenght)

#         if pre_sum not in hash:
#             hash[pre_sum] = i

#     return max_len






# nums = [10, 5, 2, 7, 1, 9]
# k=15
# print(longest_subarray(nums,k))

def longest_subarray(nums,k):
    n = len(nums)

    left = 0
    right = 0
    pre_sum = nums[0]
    max_len = 0

    while right < n:
        while left <= right and pre_sum > k:
            pre_sum -= nums[left]
            left += 1


        if pre_sum == k:
            max_len = max(max_len,right-left+1)

        right += 1

        if pre_sum < k:
            pre_sum += nums[right]

    return max_len
                
nums = [10, 5, 2, 7, 1, 9]
k=15
print(longest_subarray(nums,k))


