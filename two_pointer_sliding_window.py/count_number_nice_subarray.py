# Brute Force

'''def count_nice_subarray(nums,k):
    n = len(nums)
    count = 0

    for i in range(n):
        odd_nice = 0
        for j in range(i,n):
            if nums[j] % 2 != 0:
                odd_nice += 1


            if odd_nice > k:
                break

            if odd_nice == k:
                count += 1

    return count
    
          
# nums = [1,1,2,1,1]
# k = 3
# nums = [2,4,6]
# k = 1
nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(count_nice_subarray(nums,k))'''

# Better. //Prefix_sum + Hashing//

'''def count_nice_subarray(nums,k):
    odd_count = 0
    freq = {0:1}
    res = 0

    for num in nums:
        if num % 2 == 1:
            odd_count += 1

        res += freq.get(odd_count-k,0)
        freq[odd_count] = freq.get(odd_count,0)+1

    return res

nums = [1,1,2,1,1]
k = 3
# nums = [2,4,6]
# k = 1
# nums = [2,2,2,1,2,2,1,2,2,2]
# k = 2
print(count_nice_subarray(nums,k))'''

# Optimal Solution

def count_nice_subarray(nums,k):
    n = len(nums)
    max_len = 0
    left = 0

    for right in range(n):
        if nums[right] % 2 == 1:
            k -= 1


        while k < 0:
            if nums[left] % 2 == 1:
                k += 1
            left += 1


        max_len += right - left +1
    return max_len

def coun(nums,k):
    return count_nice_subarray(nums,k) - count_nice_subarray(nums,k-1)
# nums = [1,1,2,1,1]
# k = 3
nums = [2,4,6]
k = 1
# nums = [2,2,2,1,2,2,1,2,2,2]
# k = 2
print(coun(nums,k))

