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


# def three_sum(nums):
#     nums.sort()
#     n = len(nums)
#     st = []
#     i = 0

#     for i in range(n):
#         if i >= 0 and nums[i] == nums[i-1]:
#             continue

#         j = i + 1
#         k = n-1

#         while j < k:
#             total = nums[i]+nums[j]+nums[k]

#             if total < 0:
#                 j += 1
            
#             elif total > 0:
#                 k -= 1

#             else:
#                 st.append([nums[i],nums[j],nums[k]])
#                 j += 1
#                 k -= 1

#                 while j < k and nums[j] == nums[j-1]:
#                     j += 1
#                 while j < k and nums[k] == nums[k-1]:
#                     k -= 1

#     return st


# nums = [-1,0,1,2,-1,-4]
# print(three_sum(nums))

# def appers_once(nums):
#     n = len(nums)

#     for i in range(n):
#         num = nums[i]
#         count = 0

#         for j in range(n):
#             if nums[j] == num:
#                 count += 1

#         if count == 1:
#             return num
# # nums = [1, 2, 2, 4, 3, 1, 4]
# nums = [5]

# print(appers_once(nums))


# def appers_once(nums):
#     n = len(nums)
#     d = {}

#     for i in range(n):
#         if nums[i] not in d:
#             d[nums[i]] = 1
#         else:
#             d[nums[i]] += 1

#     for key,value in d.items():
#         if value == 1:
#             return key



# nums = [1, 2, 2, 4, 3, 1, 4]
# nums=  [5]

# print(appers_once(nums))

# def appers_once(nums):
#     n = len(nums)
#     xorr = 0

#     for i in range(n):
#         xorr ^= nums[i]

#     return xorr



# nums = [1, 2, 2, 4, 3, 1, 4]
# # nums=  [5]

# print(appers_once(nums))


# def majority_element(nums):
#     n = len(nums)

#     for i in range(n):
#         num = nums[i]
#         count = 0
#         for j in range(n):
#             if nums[j] == num:
#                 count += 1

#         if count > n//2:
#             return num



# # nums = [2,2,1,1,1,2,2]
# nums = [3,2,3]
# print(majority_element(nums))

# def majority_element(nums):
#     n = len(nums)
#     d = {}

#     for i in range(n):
#         if nums[i] not in d:
#             d[nums[i]] = 1
#         else:
#             d[nums[i]] += 1

#     for key,value in d.items():
#         if value > n//2:
#             return key

# # nums = [2,2,1,1,1,2,2]
# nums = [3,2,3]
        
        
# def majority_element(nums):
#     n = len(nums)
#     element = None
#     count = 0
#     for i in range(n):
#         if count == 0:
#             count = 1
#         element = nums[i]

#         if nums[i] == element:
#             count += 1
#         else:
#             count -= 1
#     count = 0
#     for i in range(n):
#         if nums[i] == element:
#             count += 1

#     if count > n//2:
#         return element
#     else:
#         return -1

# # nums = [2,2,1,1,1,2,2]
# # nums = [3,2,3]
# nums = [1,2,2,4,3,1,4]
# print(majority_element(nums))

# def max_subarray(nums):
#     n = len(nums)
#     max_len = 0

#     for i in range(n):

#         sum = 0
#         for j in range(i,n):
#             sum += nums[j]

#             if sum == k:
#                 max_len = max(max_len, j-i+1)
#     return max_len


# nums = [10, 5, 2, 7, 1, 9]
# k=15
# print(max_subarray(nums))


# def max_subarray(nums,k):
#     n = len(nums)
#     d = {0:-1}
#     max_len = 0
#     prefix_sum = 0

#     for i in range(n):
#         prefix_sum += nums[i]

#         # if prefix_sum == 0:
#             # max_len = i + 1


#         if prefix_sum-k in d:
#             max_len = max(max_len,i-d[prefix_sum-k] )
        
#         if prefix_sum not in d:
#             d[prefix_sum] = i



#     return max_len


# # nums = [10, 5, 2, 7, 1, 9]
# nums = [1, -1, 5, -2, 3]
# k=3
# print(max_subarray(nums,k))

# compute length of the longest subarray with sum 0
# def maxLen(A: list[int], n: int) -> int:
#     # map prefix sum -> first index seen
#     mpp: dict[int, int] = {}
#     # best length so far
#     maxi = 0
#     # running prefix sum
#     s = 0

#     # iterate over the array
#     for i in range(n):
#         # update running sum
#         s += A[i]

#         # if sum is zero, subarray [0..i] has zero sum
#         if s == 0:
#             # update best length
#             maxi = i + 1
#         # otherwise check if this sum was seen before
#         else:
#             # when seen, zero-sum segment between previous index + 1 and i
#             if s in mpp:
#                 # maximize length
#                 maxi = max(maxi, i - mpp[s])
#             # first time seeing this sum
#             else:
#                 # record index
#                 mpp[s] = i

#     # return best length
#     return maxi

# # program entry
# def main():
#     # sample input
#     A = [9, -3, 3, -1, 6, -5]
#     # compute size
#     n = len(A)
#     # print result
#     print(maxLen(A, n))

# # run main
# if __name__ == "__main__":
#     main()


def max_subarray(nums,k):
    n = len(nums)
    d = {0:-1}
    max_len = 0
    prefix_sum = 0

    for i in range(n):
        prefix_sum += nums[i]

        if prefix_sum - k in d:
            max_len = max(max_len,i-d[prefix_sum-k])

        if prefix_sum not in d:
            d[prefix_sum] = i
    
    return max_len


# nums = [10, 5, 2, 7, 1, 9]
nums = [1, -1, 5, -2, 3]
k=3
print(max_subarray(nums,k))












