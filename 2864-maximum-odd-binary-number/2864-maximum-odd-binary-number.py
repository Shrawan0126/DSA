class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_one = 0
        count_zero = 0

        for c in s:
            if c == '0' : count_zero += 1
            else : count_one += 1

        res = ""

        while count_one > 1 :
            res += "1"
            count_one -= 1
        while count_zero > 0:
            res += "0"
            count_zero -= 1

        res += "1"

        return res