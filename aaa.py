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


'''def fun(i,n):
    if i > n:
        return 0

    # print(i)
    fun(i+1,n)
    print(i)

fun(1,5)'''

# def linear_ser(nums,target):
#     n = len(nums)

#     for i in range(n):
#         if nums[i] == target:
#             return i

#     return -1



# nums = [1,2,3,4,5]
# target = 6
# print(linear_ser(nums,target))

'''def union_sor(nums1,nums2):
    n = len(nums1)
    m = len(nums2)

    st = set()
    for i in range(n):
        st.add(nums1[i])

    for j in range(m):
        st.add(nums2[j])

    ans = []
    for k in st:
        ans.append(k)

    return ans





nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 7]
print(union_sor(nums1,nums2))'''

'''def missing_num(nums):
    n = len(nums)

    res = n*(n+1)//2
    ans = res - sum(nums)

    return ans 

# nums = [0, 2, 3, 1, 4]
# nums = [0, 1, 2, 4, 5, 6]
nums = [1, 3, 6, 4, 2, 5]
print(missing_num(nums))'''

'''def max_consecutive(nums):
    n = len(nums)

    count = 0
    max_count = 0
    for i in range(n):
        if nums[i] == 1:
            count += 1

            max_count = max(max_count, count)

        else:
            count = 0

    return max_count

nums = [1,1,0,1,1,1]
# nums = [1,0,1,1,0,1]

print(max_consecutive(nums))'''

# def max_consecutive(nums):
#     n = len(nums)
#     count = 0
#     max_count = 0

#     for i in range(n):
#         count = 0

#         for j in range(i,n):
#             if nums[j] == 1:
#                 count += 1

#             else:
#                 break

#         max_count = max(max_count, count)

#     return max_count



# # nums = [1,1,0,1,1,1]
# nums = [1,0,1,1,0,1]

# print(max_consecutive(nums))

'''def single_number(nums):
    n = len(nums)
    

    for i in range(n):
        count = 0
        for j in range(n):
            if nums[j] == nums[i]:
                count += 1


        if count == 1:
            return nums[i]

nums = [4,1,2,1,2]
print(single_number(nums))
'''

'''def single_number(nums):
    n = len(nums)

    dit = {}

    for d in nums:
        if d not in dit:
            dit[d] = 1

        else:
            dit[d] += 1

    for key,value in dit.items():
        if value == 1:
            return key



# nums = [4,1,2,1,2]
nums = [2,2,1]
print(single_number(nums))'''

# def single_number(nums):

#     xorr = 0

#     for i in range(len(nums)):
#         xorr ^= nums[i]
#     return xorr

# nums = [4,1,2,1,2]
# # nums = [2,2,1]
# print(single_number(nums))

def longest_subarray(nums,k):
    n = len(nums)
    length = 0
    max_len = 0

    for i in range(n):
        curr_sum = 0
        for j in range(i,n):
            curr_sum += nums[j]

            if curr_sum == k:
                length = j-i+1

                max_len = max(max_len, length)


    return max_len


# nums = [10, 5, 2, 7, 1, 9]
# k=15
nums = [-3, 2, 1]
k=6
print(longest_subarray(nums,k))







