class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0: 
            return []
        
        x = n // 3
        res = set()
        nums.sort()
        
        temp = nums[0]
        count = 1
        
        for i in range(1, n):
            if nums[i] == temp:
                count += 1
            else:
                if count > x:
                    res.add(temp)
                temp = nums[i]
                count = 1
                
        if count > x:
            res.add(temp)
            
        return list(res)