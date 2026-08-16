# Brute force

'''def sum_of_subarray_ranges(nums):
    n = len(nums)
    total = 0

    for i in range(n):
        a = nums[i]
        b = nums[i]
        for j in range(i,n):
            a = max(a,nums[j])
            b = min(b, nums[j])

            total += a-b

    return total

# nums = [1,2,3]
nums = [1,3,3]
print(sum_of_subarray_ranges(nums))'''


# Optimal Solution

# Find the index of the Next Smaller Element for every element
def findNSE(arr):
    n = len(arr)

    # Store the answer indices
    ans = [0] * n

    # Monotonic increasing stack
    st = []

    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        currele = arr[i]

        # Remove elements that are greater than or equal
        # to the current element
        while st and arr[st[-1]] >= currele:
            st.pop()

        # Stack top is the Next Smaller Element
        # If stack is empty, no smaller element exists
        if st:
            ans[i] = st[-1]
        else:
            ans[i] = n

        # Push current index into the stack
        st.append(i)

    return ans


# Find the index of the Next Greater Element for every element
def findNGE(arr):
    n = len(arr)

    # Store the answer indices
    ans = [0] * n

    # Monotonic decreasing stack
    st = []

    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        currele = arr[i]

        # Remove elements that are smaller than or equal
        # to the current element
        while st and arr[st[-1]] <= currele:
            st.pop()

        # Stack top is the Next Greater Element
        # If stack is empty, no greater element exists
        if st:
            ans[i] = st[-1]
        else:
            ans[i] = n

        # Push current index into the stack
        st.append(i)

    return ans


# Find the index of the Previous Smaller or Equal Element
def findPSEE(arr):
    n = len(arr)

    # Store the answer indices
    ans = [0] * n

    # Monotonic increasing stack
    st = []

    # Traverse from left to right
    for i in range(n):
        currele = arr[i]

        # Remove elements that are strictly greater
        # than the current element
        while st and arr[st[-1]] > currele:
            st.pop()

        # Stack top is the Previous Smaller or Equal Element
        # If stack is empty, no such element exists
        if st:
            ans[i] = st[-1]
        else:
            ans[i] = -1

        # Push current index into the stack
        st.append(i)

    return ans


# Find the index of the Previous Greater or Equal Element
def findPGEE(arr):
    n = len(arr)

    # Store the answer indices
    ans = [0] * n

    # Monotonic decreasing stack
    st = []

    # Traverse from left to right
    for i in range(n):
        currele = arr[i]

        # Remove elements that are strictly smaller
        # than the current element
        while st and arr[st[-1]] < currele:
            st.pop()

        # Stack top is the Previous Greater or Equal Element
        # If stack is empty, no such element exists
        if st:
            ans[i] = st[-1]
        else:
            ans[i] = -1

        # Push current index into the stack
        st.append(i)

    return ans


# Find the sum of minimum elements of all subarrays
def sumSubarrayMins(arr):

    # Find Previous Smaller or Equal
    psee = findPSEE(arr)

    # Find Next Smaller
    nse = findNSE(arr)

    n = len(arr)
    total = 0

    # Calculate contribution of every element
    for i in range(n):

        # Number of choices on the left
        left = i - psee[i]

        # Number of choices on the right
        right = nse[i] - i

        # Number of subarrays where arr[i] is minimum
        freq = left * right

        # Add contribution of arr[i]
        total += freq * arr[i]

    return total


# Find the sum of maximum elements of all subarrays
def sumSubarrayMaxs(arr):

    # Find Previous Greater or Equal
    pgee = findPGEE(arr)

    # Find Next Greater
    nge = findNGE(arr)

    n = len(arr)
    total = 0

    # Calculate contribution of every element
    for i in range(n):

        # Number of choices on the left
        left = i - pgee[i]

        # Number of choices on the right
        right = nge[i] - i

        # Number of subarrays where arr[i] is maximum
        freq = left * right

        # Add contribution of arr[i]
        total += freq * arr[i]

    return total


# Sum of subarray ranges
# Range = Maximum - Minimum
def subArrayRanges(arr):

    # Sum of all maximums - Sum of all minimums
    return sumSubarrayMaxs(arr) - sumSubarrayMins(arr)


# Test the solution
arr = [1, 2, 3]

# Find the sum of subarray ranges
ans = subArrayRanges(arr)

print("The sum of subarray ranges is:", ans)

def findNSE(arr):
    n = len(arr)
    ans = [0] * n
    st = []

    for i in range(n-1, -1, -1):
        currele = arr[i]
        while st and arr[st[-1]] >= currele:
            st.pop()


        if st:
            ans[i] = st[-1]

        else:
            ans[i] = n

        st.append(i)

    return ans

def findNGE(arr):
    n = len(arr)
    ans = [0] * n
    st = []

    for i in range(n-1, -1, -1):
        currele = arr[i]
        while st and arr[st[-1]] <= currele:
            st.pop()


        if st:
            ans[i] = st[-1]

        else:
            ans[i] = n

        st.append(i)

    return ans

def findPSEE(arr):
    n = len(arr)
    ans = [0] * n
    st = []

    for i in range(n):
        currele = arr[i]
        while st and arr[st[-1]] > currele:
            st.pop()


        if st:
            ans[i] = st[-1]

        else:
            ans[i] = -1

        st.append(i)

    return ans

def findPGEE(arr):
    n = len(arr)
    ans = [0] * n
    st = []

    for i in range(n):
        currele = arr[i]
        while st and arr[st[-1]] < currele:
            st.pop()


        if st:
            ans[i] = st[-1]

        else:
            ans[i] = -1

        st.append(i)

    return ans

def sumSubarrayMins(arr):
    nse = findNSE(arr)
    psee  = findPSEE(arr)

    n = len(arr)
    total = 0

    for i in range(n):
        left = i-psee[i]
        right = nse[i] - i

        freq = left * right
        total += freq * arr[i]

    return total

def sumSubarrayMaxs(arr):
    nge = findNGE(arr)
    pgee  = findPGEE(arr)

    n = len(arr)
    total = 0

    for i in range(n):
        left = i-pgee[i]
        right = nge[i] - i

        freq = left * right
        total += freq * arr[i]

    return total

def subArrayRanges(arr):
    return sumSubarrayMaxs(arr) - sumSubarrayMins(arr)


arr = [1,2,3]
ans = subArrayRanges(arr)
print("The sum of subarray ranges is:", ans)