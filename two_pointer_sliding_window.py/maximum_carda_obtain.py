# Brute Force

# def maximum_cards(cardspoints,k):
#     n = len(cardspoints)
#     max_len = 0

#     for i in range(k+1):
#         temp_sum = 0
#         for j in range(i):
#             temp_sum += cardspoints[j]

#         for j in range(k-i):
#             temp_sum += cardspoints[n-1-j]


#         max_len = max(max_len,temp_sum)

#     return max_len

# # cardspoints = [1,2,3,4,5,6,1]
# # k = 3
# # cards = [2,2,2]
# cardspoints = [9,7,7,9,7,7,9]
# k = 7

# k = 2
# print(maximum_cards(cardspoints,k))

# Optimization Force

# def cardspoints(cardPoints):
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
# print(cardspoints(cardPoints))

def longest_substring_at_most_k(s,k):
    n = len(s)
    freq = {}
    left = 0
    max_len = 0

    for right in range(n):
        freq[s[right]] = freq.get(s[right],0)+1

        while len(freq) > k:
            freq[s[left]] -= 1

            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1


        max_len = max(max_len,right-left+1)

    return max_len



s = "aababbcaacc"
# s = "abcddefg"
# k = 3

k = 2

print(longest_substring_at_most_k(s,k))

