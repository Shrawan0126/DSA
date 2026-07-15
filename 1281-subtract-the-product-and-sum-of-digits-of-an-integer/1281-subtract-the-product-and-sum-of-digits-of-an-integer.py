class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro = 1
        sum = 0
        while n > 0:
            digit = n%10
            n //= 10
            pro *= digit
            sum += digit
        
        return pro - sum