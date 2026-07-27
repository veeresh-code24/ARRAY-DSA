# Brute force

'''def largest_num(nums):
    nums.sort()

    return nums[-1]

nums = [3, 3, 6, 1]
print(largest_num(nums))


# Optimal Solution
def largest_num(nums):

    largest = float('-inf')

    for i in range(len(nums)):
        if nums[i] > largest:
            largest = nums[i]

    return largest

# nums = [3, 3, 6, 1]
nums = [0,0,0, -40]

print(largest_num(nums))

'''
# Brute Force

'''def second_lar(nums):
    nums.sort()
    largest = nums[-1]

    for i in range(len(nums)-1, -1, -1):
        if nums[i] != largest:
            return nums[i]



nums = [8, 8, 7, 6, 5]
print(second_lar(nums))

# Better 

def second_lar(nums):
    first_lar = float('-inf')
    second_lar = float('-inf')

    for i in range(len(nums)):
        if nums[i] > first_lar:
            first_lar = nums[i]

    for i in range(len(nums)):
        if nums[i] != first_lar and nums[i] > second_lar:
            second_lar = nums[i]

    return second_lar


nums = [8, 8, 7, 6, 5]
print(second_lar(nums))

# Optimal Solution

def second_lar(nums):
    fir_lar = float('-inf')
    sec_lar = float('-inf')

    

    for i in range(len(nums)):
        if nums[i] > fir_lar:
            sec_lar = fir_lar
            fir_lar = nums[i]



        elif nums[i] != fir_lar and nums[i] > sec_lar:
            sec_lar = nums[i]

    if sec_lar == float('-inf'):
        return -1


    return sec_lar

# nums = [8, 8, 7, 6, 5]
nums = [10, 10, 10, 10, 10]
# nums = [7, 7, 2, 2, 10, 10, 10]
print(second_lar(nums))
'''

# def check_sort(nums):

#     for i in range(1,len(nums)):
#         if nums[i] < nums[i-1]:
#             return False

#     return True


# nums = [1,2,3,5]
# print(check_sort(nums))

# Brute Force

'''def rem_dupli(nums):

    st = set()
    for i in range(len(nums)):
        st.add(nums[i])

    index = 0

    for i in st:
        nums[index] = i
        index += 1

    return index


# nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
print(rem_dupli(nums))

# Optimal

def rem_dupli(nums):
    n = len(nums)

    i = 0
    for j in range(n):
        if nums[j] != nums[i]:
            nums[i+1] = nums[j]
            i += 1

    return i + 1


nums = [1,1,2]
# nums = [0,0,1,1,1,2,2,3,3,4]
print(rem_dupli(nums))
'''

'''def left_rot_one(nums):

    n = len(nums)
    temp = nums[0]

    for i in range(1,n):
        nums[i-1] = nums[i]

    nums[-1] = temp
    return nums



# nums = [1, 2, 3, 4, 5]
nums = [-1, 0, 3, 6]
print(left_rot_one(nums))

# Better

def left_rot_one(nums,k):
    n = len(nums)
    temp = nums[0:k]
    k = k % n

    for i in range(k,n):
        nums[i-k] = nums[i]

    for  i in range(k):
        nums[n-k+i] = temp[i]

    return nums


nums = [1, 2, 3, 4, 5]
# nums = [-1, 0, 3, 6]
k = 3
print(left_rot_one(nums,k))

# Optimal

def left_rot_one(nums,k):
    n = len(nums)

    k = k%n

    nums[:k] = reversed(nums[:k])
    nums[k:]  = reversed(nums[k:])
    nums[::] = nums[::-1]

    return nums

nums = [1, 2, 3, 4, 5]
# nums = [-1, 0, 3, 6]
k = 3
print(left_rot_one(nums,k))'''

'''def left_rotate(nums,k):

    n = len(nums)
    k = k % n
    temp = nums[0:k]

    for i in range(k,n):
        nums[i-k] = nums[i]

    for i in range(k):
        nums[n-k+i] = temp[i]

    return nums



nums = [1,2,3,4,5,6,7]
k = 3
print(left_rotate(nums,k))'''

'''def left_rotate(nums,k):
    k = k % len(nums)

    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    nums[::] = nums[::-1]

    return nums


nums = [1,2,3,4,5,6,7]
k = 3
print(left_rotate(nums,k))'''

# Brute Force

# def move_zero_end(nums):
#     n = len(nums)
#     lst = []

#     for i in range(n):
#         if nums[i] != 0:
#             lst.append(nums[i])

#     for i in range(len(lst)):
#         nums[i] = lst[i]

#     for i in range(len(lst), n):
#         nums[i] = 0

#     return nums

# # nums = [0,1,0,3,12]
# nums = [0]
# print(move_zero_end(nums))

# # Optimal

# def move_zero_end(nums):
#     n = len(nums)

#     z = 0
#     nz = 0

#     while nz < n:
#         if nums[nz] != 0:
#             nums[nz],nums[z] = nums[z], nums[nz]
#             z += 1
#             nz += 1

#         else:
#             nz += 1

#     return nums



# nums = [0,1,0,3,12]
# nums = [0]
# print(move_zero_end(nums))


def fun(i,n):
    if i > n:
        return 0

    # print(i)
    fun(i+1,n)
    print(i)

fun(1,5)










