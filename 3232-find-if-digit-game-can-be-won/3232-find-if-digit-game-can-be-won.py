class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_sum = 0
        double_sum = 0
        
        for num in nums:
            if num > 9:
                double_sum += num
            else:
                single_sum += num

        return single_sum != double_sum