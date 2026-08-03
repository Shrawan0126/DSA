class Solution:
    def splitNum(self, num: int) -> int:
        num1 = 0
        num2 = 0

        Sorted_digits = sorted([int(d) for d in str(num)])

        for i in range(0,len(Sorted_digits)):
            if i%2 == 0:
                num1 = num1*10 + Sorted_digits[i]
            else : 
                num2 = num2*10 + Sorted_digits[i]

        return num1+num2
            