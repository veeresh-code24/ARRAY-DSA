'''def largest_odd_number(nums):

    res = ""
    for num in "35427":
        if int(num) % 2 == 1:
            res += num

    return res
nums = "35427"

print(largest_odd_number(nums))'''

# Better

def largest_odd_number(nums):
    n = len(nums)

    i = 0


    for i in range(n-1,-1,-1):
        if int(nums[i]) % 2 == 1:
            ind = i
            break

    i = 0
    while i <= ind and nums[i] == '0':
        i += 1
    return nums[i:ind+1]


nums = "003000"

print(largest_odd_number(nums))

