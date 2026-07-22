class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        score = 0

        for i in range(0,k):
            last = nums.pop()
            nums.append(last+1)
            score += last

        return score