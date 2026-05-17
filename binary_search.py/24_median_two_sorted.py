# Brute Force Appr

'''class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        arr=[]
        while i<len(nums1) and j <len(nums2):
            if nums1[i]<=nums2[j]:
                arr.append(nums1[i])
                i+=1
            
            else:
                arr.append(nums2[j])
                j+=1
        
        arr.extend(nums1[i:])
        arr.extend(nums2[j:])
        n=len(arr)//2


        if len(arr)%2==1:
            return arr[n]
        
        else :

            return (arr[n]+arr[n-1])/2'''
            

        

# Optimization Approach

def findMedianSortedArray(nums1, nums2):

    # Binary search on smaller array
    if len(nums2) < len(nums1):
        return findMedianSortedArray(nums2, nums1)

    n1 = len(nums1)
    n2 = len(nums2)

    low = 0
    high = n1

    while low <= high:

        cut1 = (low + high) // 2
        cut2 = (n1 + n2 + 1) // 2 - cut1

        left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
        left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]

        right1 = float('inf') if cut1 == n1 else nums1[cut1]
        right2 = float('inf') if cut2 == n2 else nums2[cut2]

        # Correct partition
        if left1 <= right2 and left2 <= right1:

            # Even length
            if (n1 + n2) % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2

            # Odd length
            else:
                return max(left1, left2)

        # Move left
        elif left1 > right2:
            high = cut1 - 1

        # Move right
        else:
            low = cut1 + 1

    return 0.0


nums1 = [1, 3]
nums2 = [2,7,10]

print(findMedianSortedArray(nums1, nums2))


# Approach	       Time	    Space
# Merge Array	       O(n+m)	    O(n+m)
# Binary Search 	   O(log(min(n,m)))	O(1)
# Partition
