# Brute

'''def merge_sorted_array(nums1,nums2,m,n):
    arr = []

    for i in range(m):
        arr.append(nums1[i])

    for i in range(n):
        arr.append(nums2[i])

    for i in range(len(arr)):
        nums1[i] = arr[i]

    return sorted(nums1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge_sorted_array(nums1,nums2,m,n))'''


'''def merge_sorted_array(nums1,nums2,m,n):
   arr = [0] * (n+m)
    left = 0
    right = 0
    index = 0
    while left < m and right < n:
        if nums1[left] <= nums2[right]:
            arr[index] = nums1[left]
            index += 1
            left += 1

        else:

            arr[index] = nums2[right]
            index += 1
            right += 1

    while left < m:
        arr[index] = nums1[left]
        index += 1
        left += 1

    while right < n:
        arr[index] = nums2[right]
        index += 1
        right += 1

    for i in range(n+m):
        nums1[i] = arr[i]
    
    return nums1
   
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge_sorted_array(nums1,nums2,m,n))'''



def merge_sorted_array(nums1,nums2,m,n):
    left = m-1
    right = 0


    while left < 0 and right < n:
        if nums1[left] > nums2[right]:
            nums1[left],nums2[right] = nums2[right],nums1[left]
            left -= 1
            right += 1

        else:
            break

    nums1.sort()
    nums2.sort()

    return nums1,nums2


   

nums1 = [1,2,2]
m = 3
nums2 = [2,5,6]
n = 3
print(merge_sorted_array(nums1,nums2,m,n))



