# Brute Approach

# Function to check whether bouquets can be made
'''def is_possible(bloom_days, day, m, k):

    count = 0
    bouquets = 0

    for bloom in bloom_days:

        # Flower is bloomed
        if bloom <= day:
            count += 1

            # Enough adjacent flowers for 1 bouquet
            if count == k:
                bouquets += 1
                count = 0

        # Adjacency breaks
        else:
            count = 0

    return bouquets >= m


# Main function
def min_days_to_make_bouquets(bloom_days, m, k):

    total_flowers = m * k

    # Not enough flowers
    if total_flowers > len(bloom_days):
        return -1

    low = min(bloom_days)
    high = max(bloom_days)

    # Check every day
    for day in range(low, high + 1):

        possible = is_possible(bloom_days, day, m, k)

        if possible:
            return day

    return -1


# Example usage
bloom_days = [7, 7, 7, 7, 13, 11, 12, 7]

m = 2
k = 3

result = min_days_to_make_bouquets(bloom_days, m, k)

if result == -1:
    print("We cannot make m bouquets")

else:
    print("Minimum day is:", result)'''


# BRUTE TWO
'''def minimum_bouquete(bloomDay,day,m,k):
    count = 0
    bouquete = 0

    for bloom in bloomDay:
        if bloom <= day:
            count += 1
            if count == k:
                bouquete += 1
                count = 0

        else:
            count = 0

    return bouquete >= m

def mini(bloomDay,m,k):
    total_flower = m*k

    if total_flower > len(bloomDay):
        return -1
    
    low = min(bloomDay)
    high = max(bloomDay)

    for day in range(low,high+1):
        possible = minimum_bouquete(bloomDay,day,m,k)

        if possible:
            return day
        
    return -1


bloomDay = [1,10,3,10,2]
m = 3
k = 1
print(mini(bloomDay,m,k))'''


def is_possible(bloomday,day,m,k):
    count = 0
    bouq = 0

    for bloom in bloomday:
        if bloom <= day:
            count += 1
            if count == k:
                bouq += 1
                count = 0
        else:
            count = 0

    return bouq >= m

def minimum(bloomday,m,k):
    total_flower = m*k

    if total_flower > len(bloomday):
        return -1
    
    low = min(bloomday)
    high = max(bloomday)

    for day in range(low, high+1):
        possible = is_possible(bloomday,day,m,k)

        if possible:
            return day
        

    return -1

    
bloomday = [7,7,7,7,13,11,12,7]
m = 2
k = 3
print(minimum(bloomday,m,k))


# Optimize


# Function to check if we can form m bouquets by 'day'
'''def is_possible(bloom_days, day, m, k):

    count = 0
    bouquets = 0

    for bloom in bloom_days:

        if bloom <= day:
            count += 1

            if count == k:
                bouquets += 1
                count = 0

        else:
            count = 0

    return bouquets >= m


# Main function to find minimum day
def rose_garden(bloom_days, k, m):

    if m * k > len(bloom_days):
        return -1

    low = min(bloom_days)
    high = max(bloom_days)

    answer = -1

    while low <= high:

        mid = (low + high) // 2

        possible = is_possible(bloom_days, mid, m, k)

        if possible:
            answer = mid
            high = mid - 1

        else:
            low = mid + 1

    return answer


# Driver code
bloom_days = [7, 7, 7, 7, 13, 11, 12, 7]

k = 3
m = 2

result = rose_garden(bloom_days, k, m)

if result == -1:
    print("We cannot make m bouquets.")

else:
    print("We can make bouquets on day", result)'''


def is_possible(bloomday,day,m,k):

    count = 0
    bouqe = 0
    for bloom in bloomday:
        if bloom <= day:
            count += 1
            if count == k:
                bouqe += 1
                count = 0
        else:
            count = 0

    return bouqe  >= m


def rose_garden(bloomday,m,k):
    if m*k > len(bloomday):
        return -1
    
    low = min(bloomday)
    high = max(bloomday)
    ans = -1

    while low <= high:
        mid = (low+high)//2

        possible = is_possible(bloomday,mid,m,k)

        if possible:
            ans = mid
            high = mid-1

        else:
            low = mid+1

    return ans

bloomday = [7, 7, 7, 7, 13, 11, 12, 7]
k = 4
m = 2
print(rose_garden(bloomday,m,k))
