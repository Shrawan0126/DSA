class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for amount in accounts:
            res = max(res, sum(amount))

        return res
        