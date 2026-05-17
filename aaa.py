'''def rotaed_sorted(nums):

    for i in range(1,len(nums)):
        if nums[i-1] > nums[i]:
            return nums[i]


nums = [4, 5, 6, 7, 0, 1, 2, 3]
print(rotaed_sorted(nums))

def rotaed_sorted(nums):
    n = len(nums)

    low,high=0,n-1
    ans = float('inf')

    while low <= high:
        mid = (low+high)//2

        print(f"low={low}, mid={mid}, high={high}, ans={ans}")

        if nums[low] <= nums[mid]:
            ans = min(ans,nums[low])
            low = mid+1

        else:
            ans = min(ans,nums[mid])
            high = mid-1

    return ans

nums = [4, 5, 6, 7,0, 1, 2, 3]
print(rotaed_sorted(nums))

def rotaed_sorted(nums):
    n = len(nums)

    low,high=0,n-1

    while low < high:
        mid = (low+high)//2

        print(f"low:{low}, mid :{mid}, high:{high}")


        if nums[mid] > nums[high]:
            low = mid + 1

        else:
            high = mid

    return low

nums = [0, 1, 2, 3]
print(rotaed_sorted(nums))'''

'''def single_element(nums):
    n = len(nums)
    xorr = 0

    for i in range(n):
        xorr ^= nums[i]

    return xorr


nums = [1,1,2,3,3,4,4,8,8]
print(single_element(nums))'''


'''def single_element(nums):
    n = len(nums)

    if n == 1:
        return nums[0]
    
    if nums[0] != nums[1]:
        return nums[0]
    
    if nums[n-1] != nums[n-2]:
        return nums[n-1]
    
    low,high = 1,n-2

    while low <= high:
        mid = (low+high)//2

        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]
        
        if ((mid%2==1 and nums[mid-1] == nums[mid]) or
            (mid%2==0 and nums[mid] == nums[mid+1])):
            
            low = mid+1

        else:
            high = mid-1

    return -1


nums = [1,1,2,3,3,4,4,8,8]
print(single_element(nums))'''


'''def single_element(nums):
    n = len(nums)

    if n == 1:
        return nums[0]
    
    if nums[0] != nums[1]:
        return nums[0]
    
    if nums[n-1] != nums[n-2]:
        return nums[n-1]

    for i in range(1,n-2):
        if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
            return nums[i]



nums = [1,1,2,2,3,3,4,4,8,8,9]
print(single_element(nums))'''

'''def peak_element(nums):
    n = len(nums)

    for i in range(n):
        if nums[i] > nums[i+1]:
            return nums[i+1]


nums = [1,2,1,3,5,6,4]
print(peak_element(nums))'''

'''def peak_element(nums):
    n = len(nums)

    if n == 1:
        return nums[0]

    if nums[0] > nums[1]:
        return 0
    
    if nums[n-1] > nums[n-2]:
        return n-1
    
    low,high = 1,n-2
    while low < high:
        mid = (low+high)//2

        # if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            # return mid
        
        if nums[mid] < nums[mid+1]:
            low = mid+1

        else:
            high = mid

    return low

nums = [1,2,1,3,5,6,4]
print(peak_element(nums))

# nums = [1,2,1,3,5,6,4]
# print(peak_element(nums))'''


# def find_square(n):
#     ans = -1

#     for i in range(1,n+1):
#         if i *i <= n:
#             ans = i

#         else:
#             break

#     return ans
# n = 28
# print(find_square(n))

'''def find_square(n):
    low,high = 1,n
    ans = -1

    while low <= high:
        mid = (low+high)//2
        
        if mid*mid <= n:
            ans = mid
            low = mid+1
        

        else:
            high = mid-1

    return high

n = 36
print(find_square(n))'''


'''def nthRoot_number(n,m):

    for i in range(1,m):
        if i**n == m:
            return i
        
        elif i**n > m:
            break

    return -1


n = 3
m = 8
print(nthRoot_number(n,m))

def nthRoot_number(n,m):
    low,high = 1,m

    while low <= high:
        mid = (low+high)//2

        if mid**n == m:
            return mid
        
        elif mid**n < m:
            low = mid+1

        else:
            high = mid-1

    return -1

n = 3
m = 27
print(nthRoot_number(n,m))'''

'''import math
def koko_eating_banana(piles,h):

    for k in range(1,max(piles)):
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile/k)

        if total_hours <= h:
            return k


piles = [3,6,7,11]
h = 8
print(koko_eating_banana(piles,h))'''

'''import math
def koko_eating_banana(piles,h):
    low,high = 1,max(piles)

    while low <= high:
        mid = (low+high)//2

        total_hours = 0

        for pile in piles:
            total_hours += math.ceil(pile/mid)

            if total_hours <= h:
                high = mid-1

            else:
                low = mid+1

    return low


piles = [3,6,7,11]
h = 8
print(koko_eating_banana(piles,h))'''

'''def make_m_boucquete(bloomday,m,k,day):

    boucq = 0
    count = 0

    for i in range(len(bloomday)):
        if bloomday[i] <= day:
            count += 1

            if count == k:
                boucq += 1
                count = 0

        else:
            count = 0

    return boucq >= m
        
def no_of_day(bloomday,m,k):
    
    if m * k > len(bloomday):
        return -1
    low = min(bloomday)
    high = max(bloomday)
    
    for day in range(low,high+1):

        possible = make_m_boucquete(bloomday,m,k,day)

        if possible:
            return day
        
    return -1


bloomday = [7,7,7,7,12,7,7]
m = 2
k = 3
print(no_of_day(bloomday,m,k))'''

'''def make_m_boucquete(bloomday,m,k,day):

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

def days_in_bloom(bloomday,m,k):

    total_flower = m*k

    if total_flower > len(bloomday):
        return -1
    
    low = min(bloomday)
    high = max(bloomday)

    while low <= high:
        mid = (low+high)//2

        if make_m_boucquete(bloomday,m,k,mid):
            ans = mid
            high = mid-1

        else:
            low = mid+1

    return ans

# bloomday = [7,7,7,7,12,7,7]
# m = 2
# k = 3
# bloomday = [1,10,3,10,2]
# m = 3
# k = 2
bloomday = [1,10,3,10,2]
m = 3
k = 1
print(days_in_bloom(bloomday,m,k))'''

# import math
'''def findSmallestDivisior(nums,threshold):
    n = len(nums)

    for thre in range(1,max(nums)+1):
        divi = 0
        for num in nums:
            divi += math.ceil(num/thre)

        if divi <= threshold:
            return thre


# nums = [1,2,5,9]
# threshold = 6
nums = [44,22,33,11,1]
threshold = 5
print(findSmallestDivisior(nums,threshold))'''

import math
def findSmallestDivisior(nums,threshold):
    n = len(nums)

    low,high = 1,max(nums)

    while low <= high:
        mid = (low+high)//2

        print(f"low={low}, mid={mid}, high={high}")

        divisor = 0

        for num in nums:
            divisor += math.ceil(num/mid)
            
        if divisor <= threshold:
            ans = mid
            high = mid-1

        else:
            low = mid+1

        print(f"low={low}, mid={mid}, high={high}")


        
    return low


nums = [1,2,5,9]
threshold = 6
# nums = [44,22,33,11,1]
# threshold = 5
print(findSmallestDivisior(nums,threshold))














