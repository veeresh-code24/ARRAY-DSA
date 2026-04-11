# Brute

def merge_sorted_array(nums1,nums2,m,n):
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
print(merge_sorted_array(nums1,nums2,m,n))