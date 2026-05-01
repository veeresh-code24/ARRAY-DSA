def subarray_with_k_diff_inte(nums,k):
    n = len(nums)
    max_count = 0

    for i in range(n):
        st = {}
        for j in range(i,n):
            st[nums[j]] = st.get(nums[j],0)+1

            if len(st) == k:
                max_count += 1
            elif len(st) > k:
                break

    return max_count

nums = [1,2,1,2,3]
k = 2
print(subarray_with_k_diff_inte(nums,k))

# Optimal

def with_differnt_integer(nums,k):
    n = len(nums)
    d = {}
    left = 0
    count = 0

    for right in range(n):
        if nums[right] not in d or d[nums[right]] == 0:
            k -= 1

        d[nums[right]] = d.get(nums[right],0)+1

        while k < 0:
            d[nums[left]] -= 1

            if d[nums[left]] == 0:
                    k += 1
            left += 1

        count += (right-left+1)

    return count

def new_count(nums,k):
    return with_differnt_integer(nums,k) - with_differnt_integer(nums,k-1)


nums = [1,2,1,2,3]
k = 2
print(new_count(nums,k))
