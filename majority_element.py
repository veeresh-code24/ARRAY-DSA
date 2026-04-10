# brute force

'''class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 1

            else:
                d[num] += 1

        for key,value in d.items():
            if value > n//2:
                return key

# optimal force
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        element = None
        count = 0

        for num in nums:
            if count == 0:
                element = num

            if num == element:
                count += 1
            else:
                count -= 1

        total = 0
        for num in nums:
            if num == element:
                total += 1

        if total > n // 2:
            return element'''