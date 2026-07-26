class Solution:
    def minMaxDifference(self, num: int) -> int:
        digits = [int(d) for d in str(num)]
        digits2 = digits.copy()
        t = 9
        for i in range(0,len(digits)):
            if digits[i] != 9:
                t = digits[i]
                break
        zero = digits[0]

        for i in range(0,len(digits)):
            if digits[i] == t:
                digits[i] = 9
            if digits2[i] == zero:
                digits2[i] = 0

        return int("".join(map(str, digits))) - int("".join(map(str, digits2)))