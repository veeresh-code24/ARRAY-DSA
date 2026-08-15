# Brute Force 1

'''def next_greater_element(nums):
    n = len(nums)
    nge = [-1] * n

    for i in range(n):
        for j in range(i+1, n):
            if nums[j] > nums[i]:
                nge[i] = nums[j]
                break

    return nge


nums = [6, 0, 8, 1, 3]    
print(next_greater_element(nums))'''

# Optimal

def next_greater_element(nums):
    n = len(nums)
    stack = []
    nge = [-1] * n

    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()


        if not stack:
            nge[i] = -1

        else:
            nge[i] = stack[-1]

        stack.append(nums[i])

    return nge




nums = [6, 0, 8, 1, 3]    
print(next_greater_element(nums))



'''def next_greater_element(nums1, nums2):
    lst = []

    for i in range(len(nums1)):
        for j in range(len(nums2)):

            if nums1[i] == nums2[j]:
                found = False

                for k in range(j+1, len(nums2)):
                    if nums2[k] > nums1[i]:
                        lst.append(nums2[k])
                        found = True
                        break

                if not found:
                    lst.append(-1)

                break


    return lst


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

print(next_greater_element(nums1, nums2))'''

'''def next_greater_element(nums):
    n = len(nums)
    nge = [-1] * n


    for i in range(n):
        for j in range(i+1, n):
            if nums[j] > nums[i]:
                nge[i] = nums[j]
                break

    return nge



nums = [6, 0, 8, 1, 3]
print(next_greater_element(nums))'''


