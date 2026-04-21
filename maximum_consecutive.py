def maximum_consective(nums):
    n = len(nums)
    max_len = 0
    count = 0

    for i in range(n):
        if nums[i] == 1:
            count += 1

            max_len = max(max_len,count)

        else:
            count = 0

    return max_len

nums = [1,1,1,1,0,1,1,10,1,1,1,1,1]
print(maximum_consective(nums))