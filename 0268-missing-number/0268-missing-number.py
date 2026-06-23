class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        total = l
        sum = 0

        for i in range(l):
            total += i
            sum += nums[i]

        return total - sum