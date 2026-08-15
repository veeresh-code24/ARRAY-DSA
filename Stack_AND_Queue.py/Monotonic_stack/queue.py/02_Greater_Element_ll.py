# Brute Force

'''def nge_element__ll(nums):
    n = len(nums)
    nge = [-1] * n

    for i in range(n):
        for j in range(1, n):
            index = (i+j) % n

            if nums[index] > nums[i]:
                nge[i] = nums[index]
                break

    return nge

nums = [6,0,8,1,3]
print(nge_element_ll(nums))'''

# Optimal

def nge_element_ll(nums):
    n = len(nums)
    nge = [-1] * n
    stack = []

    for i in range(2 * n-1, -1, -1):
        while stack and stack[-1] <= nums[i%n]:
            stack.pop()

        if stack:
            nge[i % n] = stack[-1]

        stack.append(nums[i%n])

    return nge

nums = [6,0,8,1,3]
print(nge_element_ll(nums))



