'''def subset_sum(ind, arr, ds,current_sum):
    if ind == len(arr):
        ds.append(current_sum)

        return

    subset_sum(ind+1, arr, ds,current_sum+arr[ind])


    subset_sum(ind+1, arr, ds,current_sum)


arr = [5,2,1]
ds = []
print(subset_sum(0, arr,ds,0))
print(ds)

class Solution:
    # Recursive helper function to find subset sums
    def findSums(self, index, currentSum, arr, sums):
        if index == len(arr):
            sums.append(currentSum)
            return
        # Include current element
        self.findSums(index + 1, currentSum + arr[index], arr, sums)
        # Exclude current element
        self.findSums(index + 1, currentSum, arr, sums)

    def subsetSums(self, arr):
        sums = []
        self.findSums(0, 0, arr, sums)
        sums.sort()
        return sums

# Driver code
if __name__ == "__main__":
    sol = Solution()
    arr = [5, 2, 1]
    result = sol.subsetSums(arr)
    print(*result)
'''

def subset_sum(ind, arr, current_sum, ds):
    if ind == len(arr):
        ds.append(current_sum)
        return

    subset_sum(ind+1, arr, current_sum+arr[ind], ds)

    subset_sum(ind+1, arr, current_sum, ds)



# arr = [1,2,1]
arr = [1,2,2]
ds = []
subset_sum(0, arr, 0, ds)
ds.sort()
print(ds)



    





    







    
