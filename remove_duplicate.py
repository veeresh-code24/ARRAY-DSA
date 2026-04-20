#   Brute
'''def remove_duplicate(nums):
    n = len(nums)
    st = set()

    for i in range(n):
        st.add(nums[i])

    index = 0
    for i in st:
        nums[index] = i
        index += 1

    return index
# nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,3,4]

print(remove_duplicate(nums))'''


# Optimization

def remove_duplicate(nums):
    n = len(nums)

    j = 0

    for i in range(n):
        if nums[i] != nums[j]:
            nums[j+1] = nums[i]

            j += 1

    return j + 1

# nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,3,4]

print(remove_duplicate(nums))

# Clene version 
'''def remove_duplicate(nums):
    n = len(nums)
    
    if n == 0:
        return 0

    j = 0

    for i in range(1, n):   # start from 1
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]

    return j + 1'''










