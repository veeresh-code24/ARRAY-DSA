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

def peak_element(nums):
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
# print(peak_element(nums))













