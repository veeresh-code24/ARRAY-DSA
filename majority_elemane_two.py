# Brute

# def majorty_element_two(nums):
#     n = len(nums)

#     res = []

#     for i in range(n):
#         if nums[i] not in res:
#             count = 0
#             for j in range(0,n):
#                 if nums[j] == nums[i]:
#                     count += 1

#             if count > n//3:
#                 res.append(nums[i])

#         if len(res) == 2:
#             break

#     return res
# nums = [3,2,2,3]
# print(majorty_element_two(nums))


# Better

def majorty_element_two(nums):
    n = len(nums)

    res = []
    d = {}
    mini = n//3+1

    for num in nums:
        d[num] = d.get(num,0)+1

        if d[num] == mini:
            res.append(num)

        if len(res) == 2:
            break
    return res

nums = [3,2,2,3]
print(majorty_element_two(nums))






# def majorty_element_two(nums):
#     n = len(nums)
#     d = {}


#     for i in range(n):
#         if nums[i] not in d:
#             d[nums[i]] = 1
#         else:
#             d[nums[i]] += 1



#     for key,value in d.items():
#         if value >= n//3:
#             return key


# nums = [3,2,3]
# print(majorty_element_two(nums))