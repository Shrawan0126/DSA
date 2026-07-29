class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        res = []

        for i in range(0,len(queries)):
            sum = 0
            count = 0
            for j in range(0,len(nums)):
                if sum + nums[j] <= queries[i]:
                    sum += nums[j]
                    count += 1
                else:
                    break
            res.append(count)
                
        return res