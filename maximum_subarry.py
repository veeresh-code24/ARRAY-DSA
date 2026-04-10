# Brute force

'''class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        maxi_mum = float('-inf')

        for i in range(n):

            for j in range(i,n):
                count = 0
                for k in range(i,j+1):
                    count += nums[k]


                maxi_mum = max(maxi_mum,count)

        return maxi_mum'''
    
# Better

'''class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        maxi_mum = float('-inf')

        for i in range(n):
            count = 0

            for j in range(i,n):
                count += nums[j]
                maxi_mum = max(maxi_mum,count)

        return maxi_mum'''
    


# Optimal


'''class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxi_sum = float('-inf')
        total = 0
        start = 0
        begin_start = 0
        end = 0

        for i in range(len(nums)):
            if total < 0:
                total = 0
                start = i

            total += nums[i]
            if total > maxi_sum:
                maxi_sum = total
                begin_start = start
                end = i

        print("Subarry", nums[begin_start:end+1])
        return maxi_sum'''