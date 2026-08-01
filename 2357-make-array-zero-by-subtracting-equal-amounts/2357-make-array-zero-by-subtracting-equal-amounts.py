class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
       
        temp = 0
        count = 0

        for n in nums:
            if n-temp != 0:
                temp += n-temp
                count += 1

        return count