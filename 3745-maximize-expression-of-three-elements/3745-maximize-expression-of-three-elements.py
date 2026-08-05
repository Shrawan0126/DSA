class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        x = max(nums)
        nums.remove(x)
        y = max(nums)

        return x + y - min(nums)