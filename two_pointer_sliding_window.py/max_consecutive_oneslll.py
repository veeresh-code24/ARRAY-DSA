# Brute Force

'''def max_consecutive(nums,k):
    n = len(nums)
    max_len = 0

    for i in range(n):
        zer_cou = 0
        for j in range(i,n):
            if nums[j] == 0:
                zer_cou += 1

            if zer_cou > k:
                break

            max_len = max(max_len, j-i+1)

    return max_len


# nums = nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2 
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(max_consecutive(nums,k))'''

# Optimal T--O(2N).  S-- O(1)

'''def max_consecutive(nums,k):
    n = len(nums)

    left = 0
    zero = 0
    max_len = 0

    for right in range(n):
        if nums[right] == 0:
            zero += 1

        while zero > k:
            if nums[left] == 0:
                zero -= 1

            left += 1
        max_len = max(max_len, right-left+1)
    return max_len


nums = nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2 
# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k = 3
print(max_consecutive(nums,k))'''


# Optimal Better O(n),  O(1)


def max_consecutive(nums,k):
    n = len(nums)
    left = 0
    zero = 0
    max_len = 0

    for right in range(n):
        if nums[right] == 0:
            zero += 1

        if zero > k:
            if nums[left] == 0:
                zero -= 1

            left += 1

        max_len = max(max_len, right-left+1)
    return max_len




# nums = nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2 
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(max_consecutive(nums,k))




