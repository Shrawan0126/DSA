class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort(reverse = True)
        res = []
        i = 0
        while k > 0 and i < len(nums):
            if nums[i] not in res:
                res.append(nums[i])
                k -= 1
            i += 1

        return res
