class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(str(num))
        return int(digits[0] + digits[3]) + int(digits[1] + digits[2])