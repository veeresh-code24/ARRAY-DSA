# # def count_subarray(nums,k):
# #     n = len(nums)
# #     count = 0

# #     for i in range(n):
# #         odd_number = 0
# #         for j in range(i,n):
# #             if nums[j] % 2 != 0:
# #                 odd_number += 1

# #             if odd_number == k:
# #                 count += 1
# #             elif odd_number > k:
# #                 break

# #     return count


# # # nums = [1,1,2,1,1]
# # # nums = [2,4,6]
# # # k = 1
# # # k = 3
# # nums = [2,2,2,1,2,2,1,2,2,2]
# # k = 2
# # print(count_subarray(nums,k))

# # def count_subarray(nums,k):
# #     n = len(nums)
# #     left = 0
# #     count = 0

# #     for right in range(n):
# #         if nums[right] % 2 == 1:
# #             k -= 1

# #         while  k < 0:
# #             if nums[left] % 2 == 1:
# #                 k += 1

# #             left += 1

# #         count += (right-left+1)

# #     return count

# # def total_count_subarray(nums,k):
# #     return count_subarray(nums,k) - count_subarray(nums,k-1)


# # # nums = [1,1,2,1,1]
# # # nums = [2,4,6]
# # # k = 1
# # # k = 3
# # nums = [2,2,2,1,2,2,1,2,2,2]
# # k = 2
# # print(total_count_subarray(nums,k))

# # def containing_substring(s):
# #     n = len(s)
# #     count = 0

# #     for i in range(n):
# #         d = {'a':0,'b':0,'c':0}
# #         for j in range(i,n):
# #             d[s[j]] += 1

# #             if d['a'] > 0 and d['b'] > 0 and d['c'] > 0:
# #                 count += 1

# #     return count

# # # s = "abcabc"
# # # s = "aaacb"
# # s = "abc"
# # print(containing_substring(s))

# # def containing_substring(s):
# #     n = len(s)
# #     st = [0,0,0]
# #     res = 0
# #     left = 0

# #     for right in range(n):
# #         st[ord(s[right]) - ord('a')] += 1

# #         while st[0] > 0 and st[1] > 0 and st[2] > 0:
# #             res += (len(s) - right)

# #             st[ord(s[left]) - ord('a')] -= 1
# #             left += 1

# #     return res

# # s = "abcabc"
# # # s = "aaacb"
# # # s = "abc"
# # print(containing_substring(s))

# '''def cardspoints(cardPoints):
#     n = len(cardPoints)
#     max_sum = 0

#     for i in range(k+1):
#         card_sum = 0
#         for j in range(i):
#             card_sum += cardPoints[j]

#         for j in range(k-i):
#             card_sum += cardPoints[n-1-j]

#         max_sum = max(max_sum,card_sum)

#     return max_sum

# # cardPoints = [2,2,2]
# # cardPoints = [9,7,7,9,7,7,9]
# cardPoints = [1,2,3,4,5,6,1]
# k = 3
# print(cardspoints(cardPoints))'''

# '''def cardspoints(cardPoints):
#     n = len(cardPoints)

#     total = sum(cardPoints[:k])
#     max_count = total

#     for i in range(k):
#         total -= cardPoints[k-1-i]

#         total += cardPoints[n-1-i]

#         max_count = max(max_count,total)

#     return max_count


# cardPoints = [2,2,2]
# k = 2
# print(cardspoints(cardPoints))'''

# # def with_differnt_integer(nums,k):
# #     n = len(nums)
# #     count = 0

# #     for i in range(n):
# #         d = {}
# #         for j in range(i,n):
# #             d[nums[j]] = d.get(nums[j],0)+1

# #             if len(d) == k:
# #                 count += 1
# #             elif len(d) > k:
# #                 break

# #     return count



# # nums = [1,2,1,2,3]
# # k = 2
# # print(with_differnt_integer(nums,k))

# def with_differnt_integer(nums,k):
#     n = len(nums)
#     d = {}
#     left = 0
#     count = 0

#     for right in range(n):
#         if nums[right] not in d or d[nums[right]] == 0:
#             k -= 1

#         d[nums[right]] = d.get(nums[right],0)+1

#         while k < 0:
#             d[nums[left]] -= 1

#             if d[nums[left]] == 0:
#                     k += 1
#             left += 1

#         count += (right-left+1)

#     return count

# def new_count(nums,k):
#     return with_differnt_integer(nums,k) - with_differnt_integer(nums,k-1)


# nums = [1,2,1,2,3]
# k = 2
# print(new_count(nums,k))


'''def largest(nums):
    n = len(nums)

    nums.sort()
    return nums[-1]

# nums = [3, 3, 6, 1]
nums = [3, 3, 0, 99, -40]
print(largest(nums))'''


'''def largest(nums):
    n = len(nums)

    big_ele = nums[0]

    for i in range(n):
        if nums[i] > big_ele:
            big_ele = nums[i]

    return big_ele

nums = [3, 3, 0, 99, -40]
print(largest(nums))'''

'''def sec_largest(nums):
    n = len(nums)

    nums.sort()
    sec_lar = nums[-1]

    for i in range(n-1,-1,-1):
        if nums[i] != sec_lar:
            return nums[i]
        
    return -1

# nums = [8, 8, 7, 6, 5]
nums = [10, 10, 10, 10, 10]

print(sec_largest(nums))'''

'''def sec_largest(nums):
    n = len(nums)

    fir_lar = float('-inf')
    sec_lar = float('-inf')

    for i in range(n):
        if nums[i] > fir_lar:
            fir_lar = nums[i]


    for i in range(n):
        if nums[i] > sec_lar and nums[i] != fir_lar:
            sec_lar = nums[i]

    return sec_lar

nums = [8, 8, 7, 6, 5]
nums = [10, 10, 10, 10, 10]

print(sec_largest(nums))'''

'''def sec_largest(nums):
    n = len(nums)
    first_lar = float('-inf')
    second_lar = float('-inf')

    for i in range(n):
        if nums[i] > first_lar:
            second_lar = first_lar
            first_lar = nums[i]



        elif nums[i] > second_lar and nums[i] != first_lar:
            second_lar = nums[i]

    return second_lar


# nums = [8, 8, 7, 6, 5]
nums = [10,98,-10,-40,99]

print(sec_largest(nums))'''

# def linear_ser(nums):
#     n = len(nums)

#     for i in range(n):
#         if nums[i] == target:
#             return i
        
#     return -1



# nums = [2, 3, 4, 5, 3]
# target = 3
# # nums = [2, -4, 4, 0, 10]
# # target = 6
# print(linear_ser(nums))

'''def left_rotate(nums):
    n = len(nums)
    temp =nums[:k]

    for i in range(k,n):
        nums[i-k] = nums[i]


    for i in range(n-k,n):
        nums[i] = temp[i-k-1]

    return nums


nums = [1,2,3,4,5,6,7]
k = 3
print(left_rotate(nums))'''


'''def left_rotate(nums,k):
    n = len(nums)
    k = k%n
    nums[:] = reversed(nums[::])
    # nums[k:] = reversed(nums[k:])
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    # nums[:] = reversed(nums[::])
    return nums



nums = [1,2,3,4,5,6,7]
k = 3
print(left_rotate(nums,k))'''

'''def move_zero(nums):
    n = len(nums)

    temp = []
    for i in range(n):
        if nums[i] != 0:
            temp.append(nums[i])


    for i in range(len(temp)):
        nums[i] = temp[i]

    for i in range(len(temp),n):
        nums[i] = 0

    return nums

nums = [0,1,0,3,12]
print(move_zero(nums))'''

# def move_zero(nums):
#     n = len(nums)

#     nz = 0
#     z = 0

#     for nz in range(n):
#         if nums[nz] != 0:
#             nums[nz],nums[z] = nums[z],nums[nz]
#             z += 1

#     return nums


# nums = [0,1,0,3,12]
# print(move_zero(nums))

'''def remove_dupli(nums):
    n = len(nums)

    temp = set()

    for i in range(n):
        temp.add(nums[i])

    index = 0
    for st in temp:
        nums[index] = st
        index += 1

    return index


nums = [1,1,2]
print(remove_dupli(nums))'''

'''def remove_dupli(nums):
    n = len(nums)

    i = 0
    for j in range(1,n):
        if nums[j] != nums[i]:
            nums[i+1] = nums[j]
            i += 1

    return i+1
            

nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1,1,2]
print(remove_dupli(nums))'''

'''def missing_nums(nums):
    n = len(nums)

    missing = n*(n+1)//2
    replace = sum(nums)

    return missing - replace

# nums = [0, 2, 3, 1, 4]
nums = [0, 1, 2, 4, 5, 6]
print(missing_nums(nums))'''

'''def number_appe_once(nums):
    n = len(nums)

    for i in range(n):
        num = nums[i]
        count  = 0
        for j in range(n):
            if nums[j] == num:
                count += 1

        if count == 1:
            return num


nums = [4,1,2,1,2]
print(number_appe_once(nums))'''

'''def number_appe_once(nums):
    n = len(nums)
    d = {}

    for i in range(n):
        if nums[i] not in d:
            d[nums[i]] = 1
        else:
            d[nums[i]] += 1

    for key,value in d.items():
        if value == 1:
            return key

# nums = [4,1,2,1,2]
nums = [1,1,2,2,3,3,44]
print(number_appe_once(nums))'''

'''def number_appe_once(nums):
    n = len(nums)

    xorr = 0
    for i in range(n):

        xorr ^= nums[i]

    return xorr


nums = [4,1,2,1,2]
nums = [1,1,2,2,3,3,44]
print(number_appe_once(nums))'''

'''def maajority_element(nums):
    n = len(nums)

    for i in range(n):
        num = nums[i]
        count = 0

        for j in range(n):
            if nums[j] == num:
                count += 1


        if count > n//2:
            return num

# nums = [2,2,1,1,1,2,2]
nums = [3,2,3]

print(maajority_element(nums))'''

'''def maajority_element(nums):
    n = len(nums)
    d = {}

    for i in range(n):
        if nums[i] not in d:
            d[nums[i]] = 1
        else:
            d[nums[i]] += 1

    for key,value in d.items():
        if value > n//2:
            return key


nums = [2,2,1,1,1,2,2]
# nums = [3,2,3]

print(maajority_element(nums))'''

'''def maajority_element(nums):
    n = len(nums)
    count = 0
    ele = None

    for i in range(n):
        if count == 0:
            ele = nums[i]
            count = 0

        elif ele == nums[i]:
            count += 1

        else:
            count -= 1
    maj = 0
    for i in range(n):
        if nums[i] == ele:
            maj += 1

    if maj > n//2:
        return ele


nums = [2,2,1,1,1,2,2]
# nums = [3,2,3]

print(maajority_element(nums))'''

# def count_subarry_equals_k(nums,k):
#     n = len(nums)
#     max_count = 0

#     for i in range(n):
#         count = 0
#         for j in range(i,n):
#             count += nums[j]

#             if count == k:
#                 max_count += 1

#     return max_count
 

# nums = [1,1,1]
# k = 2
# print(count_subarry_equals_k(nums,k))

'''def count_subarry_equals_k(nums,k):
    n = len(nums)
    d = {0:1}
    pre_sum = float('-inf')
    count = 0

    for num in nums:
        pre_sum += num


        if pre_sum - k in d:
            count += d[pre_sum-k]

        d[pre_sum] = d.get(pre_sum,0)+1

    return count


nums = [-1,1,1,1]
k = 2
print(count_subarry_equals_k(nums,k))'''

# def two_sum(nums,target):
#     n = len(nums)

#     for i in range(n):
#         for j in range(i+1,n):
#             if nums[i] + nums[j] == target:
#                 return i,j
            
# # nums = [2,7,11,15]
# # target = 9
# nums = [3,2,4]
# target = 6
# print(two_sum(nums,target))

# def two_sum(nums,target):
#     n = len(nums)
#     d = {}

#     for i in range(n):
#         a = nums[i]
#         mapp = target - a

#         if mapp in d:
#             return d[mapp],i
        

#         d[a] = i

# nums = [2,7,11,15]
# target = 9
# # nums = [3,2,4]
# # target = 6
# print(two_sum(nums,target))

'''def two_sum(nums,target):
    n = len(nums)
    nums.sort()

    left = 0
    right = n-1
    total = 0

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return True
        
        elif total < target:
            left += 1
        else:
            right -= 1

    return False

# nums = [2,7,11,15]
# target = 10
nums = [3,2,4]
target = 8
print(two_sum(nums,target))'''

'''def longest_subarry(nums,k):
    n = len(nums)
    d = {0:-1}
    pre_sum = float('-inf')
    max_len = 0

    for i in range(n):
        pre_sum += nums[i]

        if pre_sum - k in d:
            length = i-d[pre_sum - k]
            max_len = max(max_len,length)

        if pre_sum not in d:
            d[pre_sum] = i

    return max_len

# nums = [10, 5, 2, 7, 1, 9]
# k=15
nums = [-3, 2, 1]
k=6
print(longest_subarry(nums,k))'''

'''def longest_subarry(nums,k):
    n = len(nums)

    left = 0
    pre_sum = 0
    max_len = 0

    for right in range(n):
        pre_sum += nums[right]

        while pre_sum > k:
            pre_sum -= nums[left]
            left += 1

        if pre_sum == k:
            max_len = max(max_len,right-left+1)

    return max_len



# nums = [10, 5, 2, 7, 1, 9]
# k=15
nums = [-3, 2, 1]
k=6
print(longest_subarry(nums,k))'''

'''def max_consecutive(nums):
    n = len(nums)
    count = 0
    max_cou = 0

    for i in range(n):
        if nums[i] == 1:
            count += 1
            max_cou = max(max_cou,count)

        else:
            count = 0

    return max_cou



# nums = [1,1,0,1,1,1]
nums = [1,0,1,1,0,1]
print(max_consecutive(nums))'''

'''def rearrange_positive_negative(nums):
    n = len(nums)
    arr = [0] * n
    posi_ind = 0
    negti_ind = 1


    for i in range(n):
        if nums[i] > 0:
            arr[posi_ind] = nums[i]
            posi_ind += 2

        else:
            arr[negti_ind] = nums[i]
            negti_ind += 2

    return arr

nums = [3,1,-2,-5,2,-4]
print(rearrange_positive_negative(nums))'''

'''def max_subarray(nums):
    n = len(nums)
    max_len = float('-inf')

    for i in range(n):
        for j in range(i,n):
            sum = 0
            for k in range(i,j+1):
                sum += nums[k]

            max_len = max(max_len,sum)

    return max_len


# nums = [2, 3, 5, -2, 7, -4]
nums = [-2, -3, -7, -2, -10, -4]
print(max_subarray(nums))'''

# def max_subarray(nums):
#     n = len(nums)
#     max_len = float('-inf')

#     for i in range(n):
#         sum = 0
#         for j in range(i,n):
#             sum += nums[j]

#             max_len = max(max_len, sum)

#     return max_len

# # nums = [2, 3, 5, -2, 7, -4]
# nums = [-2, -3, -7, -2, -10, -4]
# print(max_subarray(nums))

'''def max_subarray(nums):
    n = len(nums)
    max_sum = float('-inf')
    pre_sum = 0
    start = 0
    new_start = -1
    end = -1

    for i in range(n):
        if pre_sum == 0:
            start = i

        pre_sum += nums[i]

        if pre_sum > max_sum:
            max_sum = pre_sum
            new_start = start
            end = i

        if pre_sum < 0:
            pre_sum = 0

    print(nums[new_start:end+1])
    return max_sum

nums = [2, 3, 5, -2, 7, -4]
# nums = [-2, -3, -7, -2, -10, -4]
print(max_subarray(nums))'''

'''def max_subarray_with_indices(arr):
    n = len(arr)

    maxi = float('-inf')   # same as INT_MIN
    curr_sum = 0

    start = 0
    ans_start = -1
    ans_end = -1

    for i in range(n):
        # if current sum is 0, start new subarray
        if curr_sum == 0:
            start = i

        curr_sum += arr[i]

        # update maximum
        if curr_sum > maxi:
            maxi = curr_sum
            ans_start = start
            ans_end = i

        # reset if sum becomes negative
        if curr_sum < 0:
            curr_sum = 0

    return maxi, ans_start, ans_end


# Example
# arr = [-2, -3, 4, -1, -2, 1, 5, -3]
arr = [-2, -3, -7, -2, -10, -4]
max_sum, start, end = max_subarray_with_indices(arr)

print("Max Sum:", max_sum)
print("Subarray:", arr[start:end+1])
print("Start Index:", start, "End Index:", end)'''

'''def sort(nums):
    n = len(nums)

    count,count1,count2 = 0,0,0

    for i in range(n):
        if nums[i] == 0:
            count += 1

        elif nums[i] == 1:
            count1 += 1

        else:
            count2 += 1

    for i in range(count):
        nums[i] = 0

    for i in range(count,count+count1):
        nums[i] = 1

    for i in range(count+count1,n):
        nums[i] = 2

    return nums

nums = [2,0,2,1,1,0]
# nums = [0,1,2]
print(sort(nums))'''

def sort(nums):
    n  = len(nums)
    low,mid,high = 0, 0,n-1

    while mid <= high:
        if nums[mid] == 0:
            nums[low],nums[mid] = nums[mid],nums[low]
            low += 1
            mid += 1


        elif nums[mid] == 1:
            mid += 1

        else:
            nums[mid],nums[high] = nums[high],nums[mid]
            high -= 1

    return nums



# nums = [2,0,2,1,1,0]
nums = [0,1,2]
print(sort(nums))


























