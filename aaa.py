# def sorted_array(nums1,m,nums2,n):
#     arr = []

#     for i in range(m):
#         arr.append(nums1[i])

#     for i in range(n):
#         arr.append(nums2[i])

#     arr.sort()

#     for i in range(len(arr)):
#         nums1[i] = arr[i]

#     return nums1
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# print(sorted_array(nums1,m,nums2,n))


# def sorted_array(nums1,m,nums2,n):
#     arr = [0]*(m+n)

#     left = 0
#     right = 0
#     index = 0

#     while left < m and right < n:
#         if nums1[left] < nums2[right]:
#             arr[index] = nums1[left]
#             index += 1
#             left += 1

#         else:
#             arr[index] = nums2[right]
#             index += 1
#             right += 1

#     while left < m:
#         arr[index] = nums1[left]
#         index += 1
#         left += 1

#     while right < n:
#         arr[index] = nums2[right]
#         index += 1
#         right += 1
    
#     for i in range(len(arr)):
#         nums1[i] = arr[i]

#     return nums1

# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# print(sorted_array(nums1,m,nums2,n))

def sorted_array(nums1,m,nums2,n):
    n = len(nums1)
    m = len(nums2)

    left = n-1
    right = 0

    while left >= 0 and right < m:
        if nums1[left] > nums2[right]:
            nums1[left],nums2[right]= nums2[right],nums1[left]
            left -= 1
            right += 1

        else:
            break

    nums1.sort()
    nums2.sort()

    return nums1,nums2



nums1 = [1,3,5,7]
m = 4
nums2 = [0,2,6,8,9]
n = 5
print(sorted_array(nums1,m,nums2,n))