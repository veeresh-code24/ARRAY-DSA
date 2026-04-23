# Brute
'''from itertools import permutations

def next_permutations(nums):
    n = len(nums)
    perms = sorted(set(permutations(nums)))

    current = tuple(nums)

    for i in range(len(perms)):
        if perms[i] == current:
            if i == len(perms)-1:
                return list(perms[0])
            
            return list(perms[i+1])
        
    # return nums





nums = [1, 2, 3]
# nums = [3,2,1]
# nums = [1,1,5]
print(next_permutations(nums))'''

'''from itertools import permutations
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        perms = sorted(set(permutations(nums)))
        current = tuple(nums)

        for i in range(len(perms)):
            if perms[i] == current:

                if i == len(perms)-1:
                    nums[:] = perms[0]   # ✅ in-place update
                    return

                nums[:] = perms[i+1]   # ✅ in-place update
                return'''

# Optimizations

def next_permutations(nums):
    n = len(nums)
    index = -1

    for i in range(n-2,-1,-1):
        if nums[i] < nums[i+1]:
            index = i
            break

    if index == -1:
        nums.reverse()
        return nums
        
    for i in range(n-1,-1,-1):
        if nums[i] > nums[index]:
            # break
            nums[i],nums[index] = nums[index],nums[i]
            break

    nums[index+1:] = reversed(nums[index+1:])

    return nums


# nums = [1, 2, 3]
# nums = [3,2,1]
nums = [1,1,5]
print(next_permutations(nums))


