# Brute Force

'''def canwereplace(stalls,cows,d):
    count = 1
    lastpost = stalls[0]

    for i in range(1,len(stalls)):
        if stalls[i] - lastpost >= d:
            count += 1

            lastpost = stalls[i]

        if count >= cows:
            return True
        
    return False

def aggressiveCows(stalls,cows):
    stalls.sort()

    max_dis = stalls[-1] - stalls[0]
    ans = 0

    for d in range(1,max_dis+1):
        if canwereplace(stalls,cows,d):
            ans = d

    return ans

stalls = [1, 2, 8, 4, 9]
cows = 3

print(aggressiveCows(stalls, cows))'''

# TC ---- O(n log n + max_dis * n)
# TC ---- O(max_dis * n)

'''def canreplace(stalls,cows,d):

    count = 1
    lastpos = stalls[0]

    for i in range(len(stalls)):
        if stalls[i] - lastpos >= d:
            count += 1
            lastpos = stalls[i]

        if count >= cows:
            return True
        
    return False

def aggressiveCows(stalls,cows):
    stalls.sort()
    max_dist = stalls[-1] - stalls[0]
    ans = 0

    for d in range(1, max_dist):
        if canreplace(stalls,cows,d):

            ans = d

    return ans

stalls = [1, 2, 8, 4, 9]
cows = 3
print(aggressiveCows(stalls,cows))'''

# Optimization Approach

'''def canreplace(stalls,cows,d):

    count = 1
    lastpos = stalls[0]

    for i in range(len(stalls)):
        if stalls[i] - lastpos >= d:
            count += 1

            lastpos = stalls[i]

        if count >= cows:
            return True
        
    return False

def aggressiveCows(stalls,cows):
    stalls.sort()

    low,high = 1, stalls[-1] - stalls[0]

    ans = -1

    while low <= high:
        mid = (low+high)//2

        if canreplace(stalls,cows,mid):
            ans = mid
            low = mid+1

        else:
            high = mid-1

    return high

stalls = [1, 2, 8, 4, 9]
cows = 3
print(aggressiveCows(stalls,cows))'''

# TC -- O(NlogN) + O(N * log(max(stalls[])-min(stalls[])))
# SC -- 0(1)















