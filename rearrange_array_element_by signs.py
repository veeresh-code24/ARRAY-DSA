# Brute
'''def rearrange_array(nums):
    n = len(nums)
    arr1 = []
    arr2 = []

    for i in range(n):
        if nums[i] > 0:
            arr1.append(nums[i])
        else:
            arr2.append(nums[i])


    for i in range(len(arr1)):
        nums[2*i] = arr1[i]
        nums[2*i+1] = arr2[i]

    return nums


nums = [3,1,-2,-5,2,-4]
print(rearrange_array(nums))'''

# Optimization

def rearrange_array(nums):
    n = len(nums)
    ans = [0] * n

    posi = 0
    nega = 1

    for i in range(n):
        if nums[i] < 0:
            ans[nega] = nums[i]
            nega += 2

        else:
            ans[posi] = nums[i]
            posi += 2

    return ans

        
nums = [3,1,-2,-5,2,-4]
print(rearrange_array(nums))


# If positive and negative unequal length

def rearrange_positive_negative(nums):
    pos = []
    neg = []

    for num in nums:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)

    i = j = 0
    arr = []

    while i < len(pos) and j < len(neg):
        arr.append(pos[i])
        arr.append(neg[j])
        i += 1
        j += 1

    # remaining elements
    while i < len(pos):
        arr.append(pos[i])
        i += 1

    while j < len(neg):
        arr.append(neg[j])
        j += 1

    return arr

# “Yes, using partition + rotation (harder, O(1) space)”

def right_rotate(nums, start, end):
    temp = nums[end]
    for i in range(end, start, -1):
        nums[i] = nums[i-1]
    nums[start] = temp


def rearrange(nums):
    n = len(nums)

    for i in range(n):
        # Check if index is wrong
        if (i % 2 == 0 and nums[i] < 0) or (i % 2 == 1 and nums[i] > 0):

            # Find next correct element
            j = i + 1
            while j < n:
                if (i % 2 == 0 and nums[j] > 0) or (i % 2 == 1 and nums[j] < 0):
                    break
                j += 1

            # If found → rotate
            if j < n:
                right_rotate(nums, i, j)
            else:
                break

    return nums


nums = [3, 1, -2, -5, 2, -4]
print(rearrange(nums))
