class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_one = s.count('1')
        count_zero = len(s) - count_one

        return '1' * (count_one - 1) + '0' * (count_zero) + "1"