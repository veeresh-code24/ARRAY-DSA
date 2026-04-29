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
