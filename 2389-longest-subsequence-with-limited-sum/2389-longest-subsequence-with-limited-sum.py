class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        presum = [0] * n

        for i in range(n):
            presum[i] = presum[i - 1] + nums[i] if i > 0 else nums[i]

        res = []

        for q in queries:
            l,r = 0,n-1
            while l<=r:
                mid = (l+r)//2
                if presum[mid] <= q:
                    l = mid + 1
                else:
                    r = mid - 1
            res.append(l)

        return res