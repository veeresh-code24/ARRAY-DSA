# def count_subarray(nums,k):
#     n = len(nums)
#     count = 0

#     for i in range(n):
#         odd_number = 0
#         for j in range(i,n):
#             if nums[j] % 2 != 0:
#                 odd_number += 1

#             if odd_number == k:
#                 count += 1
#             elif odd_number > k:
#                 break

#     return count


# # nums = [1,1,2,1,1]
# # nums = [2,4,6]
# # k = 1
# # k = 3
# nums = [2,2,2,1,2,2,1,2,2,2]
# k = 2
# print(count_subarray(nums,k))

# def count_subarray(nums,k):
#     n = len(nums)
#     left = 0
#     count = 0

#     for right in range(n):
#         if nums[right] % 2 == 1:
#             k -= 1

#         while  k < 0:
#             if nums[left] % 2 == 1:
#                 k += 1

#             left += 1

#         count += (right-left+1)

#     return count

# def total_count_subarray(nums,k):
#     return count_subarray(nums,k) - count_subarray(nums,k-1)


# # nums = [1,1,2,1,1]
# # nums = [2,4,6]
# # k = 1
# # k = 3
# nums = [2,2,2,1,2,2,1,2,2,2]
# k = 2
# print(total_count_subarray(nums,k))

# def containing_substring(s):
#     n = len(s)
#     count = 0

#     for i in range(n):
#         d = {'a':0,'b':0,'c':0}
#         for j in range(i,n):
#             d[s[j]] += 1

#             if d['a'] > 0 and d['b'] > 0 and d['c'] > 0:
#                 count += 1

#     return count

# # s = "abcabc"
# # s = "aaacb"
# s = "abc"
# print(containing_substring(s))

# def containing_substring(s):
#     n = len(s)
#     st = [0,0,0]
#     res = 0
#     left = 0

#     for right in range(n):
#         st[ord(s[right]) - ord('a')] += 1

#         while st[0] > 0 and st[1] > 0 and st[2] > 0:
#             res += (len(s) - right)

#             st[ord(s[left]) - ord('a')] -= 1
#             left += 1

#     return res

# s = "abcabc"
# # s = "aaacb"
# # s = "abc"
# print(containing_substring(s))

'''def cardspoints(cardPoints):
    n = len(cardPoints)
    max_sum = 0

    for i in range(k+1):
        card_sum = 0
        for j in range(i):
            card_sum += cardPoints[j]

        for j in range(k-i):
            card_sum += cardPoints[n-1-j]

        max_sum = max(max_sum,card_sum)

    return max_sum

# cardPoints = [2,2,2]
# cardPoints = [9,7,7,9,7,7,9]
cardPoints = [1,2,3,4,5,6,1]
k = 3
print(cardspoints(cardPoints))'''

'''def cardspoints(cardPoints):
    n = len(cardPoints)

    total = sum(cardPoints[:k])
    max_count = total

    for i in range(k):
        total -= cardPoints[k-1-i]

        total += cardPoints[n-1-i]

        max_count = max(max_count,total)

    return max_count


cardPoints = [2,2,2]
k = 2
print(cardspoints(cardPoints))'''

# def with_differnt_integer(nums,k):
#     n = len(nums)
#     count = 0

#     for i in range(n):
#         d = {}
#         for j in range(i,n):
#             d[nums[j]] = d.get(nums[j],0)+1

#             if len(d) == k:
#                 count += 1
#             elif len(d) > k:
#                 break

#     return count



# nums = [1,2,1,2,3]
# k = 2
# print(with_differnt_integer(nums,k))

def with_differnt_integer(nums,k):
    n = len(nums)
    d = {}
    left = 0
    count = 0

    for right in range(n):
        if nums[right] not in d or d[nums[right]] == 0:
            k -= 1

        d[nums[right]] = d.get(nums[right],0)+1

        while k < 0:
            d[nums[left]] -= 1

            if d[nums[left]] == 0:
                    k += 1
            left += 1

        count += (right-left+1)

    return count

def new_count(nums,k):
    return with_differnt_integer(nums,k) - with_differnt_integer(nums,k-1)


nums = [1,2,1,2,3]
k = 2
print(new_count(nums,k))