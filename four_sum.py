# Brute

'''def four_sum(nums,target):
    n = len(nums)
    st = set()


    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for z in range(k+1,n):
                    if nums[i] + nums[j] + nums[k] + nums[z] == target:
                        temp = tuple(sorted([nums[i],nums[j],nums[k],nums[z]]))
                        st.add(temp)

    ans = [list(x) for x in st]
    return ans

nums = [2,2,2,2,2]
target = 8
print(four_sum(nums,target))'''


# Better

'''def four_sum(nums,target):
    n = len(nums)
    st = set()

    for i in range(n):
        for j in range(i+1,n):
            hashset = set()
            for k in range(j+1,n):
                fourth = target-(nums[i]+nums[j]+nums[k])

                if fourth in hashset:
                    temp = tuple(sorted([nums[i],nums[j],nums[k],fourth]))
                    st.add(temp)

                hashset.add(nums[k])

    return [list(x) for x in st]
nums = [2,2,2,2,2]
target = 8
print(four_sum(nums,target))'''

# OPtimize


def four_sum(nums, target):
    n = len(nums)
    nums.sort()
    arr = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        for j in range(i+1, n):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                temp = nums[i] + nums[j] + nums[left] + nums[right]

                if temp == target:
                    arr.append([nums[i], nums[j], nums[left], nums[right]])

                    # skip duplicates
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    # move pointers
                    left += 1
                    right -= 1

                elif temp < target:
                    left += 1
                else:
                    right -= 1

    return arr

nums = [1, 0, -1, 0, -2, 2]
target = 0
print(four_sum(nums,target))
















