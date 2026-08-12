class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # if len(cost) == 1 : return cost[0]
        res,i = 0,0

        cost.sort(reverse=True)

        while i < len(cost) :
            res += cost[i]
            if i == len(cost)-1 : break
            res += cost[i+1]
            i += 3

        return res
