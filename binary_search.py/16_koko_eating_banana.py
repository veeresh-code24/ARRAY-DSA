# Brute Force

'''import math

def koko_eating_banana(piles,h):
    max_piles  = max(piles)

    for k in range(1,max_piles+1):
        total_hours = 0

        for pile in piles:
            total_hours += math.ceil(pile/k)

        if total_hours <= h:
            return k

h = 8
piles = [3,6,7,11]
print(koko_eating_banana(piles,h))'''

# Optimization Approach

import math
def koko_eating_banana(piles,h):

    low,high = 1, max(piles)
    ans = 0

    while low <= high:
        mid = (low+high)//2
        total_hours = 0
        for pile in piles:

            total_hours += math.ceil(pile/mid)

        if total_hours <= h:
            ans = mid
            high = mid-1

        else:
            low = mid + 1

    return ans


h = 8
piles = [3,6,7,11]
print(koko_eating_banana(piles,h))

