def maximum_cards(cards,k):
    n = len(cards)
    max_len = 0

    for i in range(k+1):
        temp_sum = 0

        for j in range(i):
            temp_sum += cards[j]

        for j in range(k-i):
            temp_sum += cards[n-1-j]

        max_len = max(max_len,temp_sum)

    return max_len

# cards = [1,2,3,4,5,6,1]
# k = 3
# cards = [2,2,2]
cards = [9,7,7,9,7,7,9]
k = 7

# k = 2
print(maximum_cards(cards,k))