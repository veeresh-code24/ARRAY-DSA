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

def triplet(n, nums):
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
print(triplet(n,nums))