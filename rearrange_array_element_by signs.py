# Brute
'''def rearrange_array(nums):
    n = len(nums)
    arr1 = []
    arr2 = []

    for i in range(n):
        if nums[i] > 0:
            arr1.append(nums[i])
        else:
            arr2.append(nums[i])


    for i in range(len(arr1)):
        nums[2*i] = arr1[i]
        nums[2*i+1] = arr2[i]

    return nums


nums = [3,1,-2,-5,2,-4]
print(rearrange_array(nums))'''

# Optimization

def rearrange_array(nums):
    n = len(nums)
    ans = [0] * n

    posi = 0
    nega = 1

    for i in range(n):
        if nums[i] < 0:
            ans[nega] = nums[i]
            nega += 2

        else:
            ans[posi] = nums[i]
            posi += 2

    return ans

        
nums = [3,1,-2,-5,2,-4]
print(rearrange_array(nums))