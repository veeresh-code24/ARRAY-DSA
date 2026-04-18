# Brute force

'''def three_sum(nums):
    n  = len(nums)
    st = set()

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i],nums[j],nums[k]]
                    temp.sort()
                    st.add(tuple(temp))

    
    ans = [list(x) for x in st]
    return ans

nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))'''

# Better 

'''def triplet(n, nums):
    st = set()

    for i in range(n):
        hashset = set()
        
        for j in range(i + 1, n):
            third = -(nums[i] + nums[j])
            
            if third in hashset:
                temp = [nums[i], nums[j], third]
                temp.sort()
                st.add(tuple(temp))   # set needs immutable → tuple
            
            hashset.add(nums[j])

    # convert set of tuples → list of lists
    ans = [list(t) for t in st]
    return ans

nums = [-1,0,1,2,-1,-4]
n =  6
print(triplet(n,nums))'''

# Optimal Solu


def three_sum(nums):
    n = len(nums)
    nums.sort()
    arr = []
    i = 0

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j = i+1
        k = n-1

        while j < k:
            target = nums[i] + nums[j] + nums[k]

            if target < 0:
                j += 1

            elif target > 0:
                k -= 1

            else:
                arr.append([nums[i],nums[j],nums[k]])
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j-1]:
                    j += 1

                while j < k and nums[k] == nums[k-1]:
                    k -= 1

    return arr


# nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
nums = [0,0,0]

print(three_sum(nums))