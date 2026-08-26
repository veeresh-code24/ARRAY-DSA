def subsetbacktrack(start, nums, current, result):

    result.append(list(current))

    for i in range(start, len(nums)):

        if i > 0 and nums[i] == nums[i-1]:
            continue

        current.append(nums[i])

        subsetbacktrack(i+1, nums, current, result)

        current.pop()

def subsetwithdupli(nums):
    nums.sort()
    result = []

    subsetbacktrack(0, nums, [], result)
    return result

nums = [1,2,2]
print(subsetwithdupli(nums))











