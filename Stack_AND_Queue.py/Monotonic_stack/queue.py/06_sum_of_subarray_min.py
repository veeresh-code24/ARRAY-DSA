# Brute Force

'''def sum_of_subarray_min(arr):
    n = len(arr)
    total = 0

    for i in range(n):
        current_min = float('inf')

        for j in range(i,n):
            current_min = min(current_min, arr[j])


            total += current_min


    return total



# arr = [3,1,2,4]
arr = [11,81,94,43,3]
print(sum_of_subarray_min(arr))'''

# Optimal Solution

def find_nse(arr):
    n = len(arr)
    nse = [n] * n
    stack = []

    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        if stack:
            nse[i] = stack[-1]

        stack.append(i)

    return nse

def find_psee(arr):
    n = len(arr)
    psee = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()

        if stack:
            psee[i] = stack[-1]

        stack.append(i)

    return psee

def sum_subarray_mins(arr):
    n = len(arr)
    nse = find_nse(arr)
    psee = find_psee(arr)

    total = 0

    for i in range(n):
        left = i - psee[i]
        right = nse[i] - i

        total += arr[i] * left * right

    return total




arr = [3, 1, 2, 5]
print(sum_subarray_mins(arr))

# 

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        n = len(arr)
        MOD = 10**9 + 7

        # Previous Smaller or Equal
        psee = [-1] * n
        stack = []

        for i in range(n):

            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                psee[i] = stack[-1]

            stack.append(i)

        # Next Smaller
        nse = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):

            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                nse[i] = stack[-1]

            stack.append(i)

        # Calculate answer
        total = 0

        for i in range(n):

            left = i - psee[i]
            right = nse[i] - i

            total += arr[i] * left * right
            total %= MOD

        return total