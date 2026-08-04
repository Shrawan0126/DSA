class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        res = []
        temp = nums[0]
        i = 1

        while temp != nums[n-1] :
            if temp+1 != nums[i]:
                res.append(temp+1)
                temp += 1
            else:
                temp = nums[i]
                i+=1
        
        return res
