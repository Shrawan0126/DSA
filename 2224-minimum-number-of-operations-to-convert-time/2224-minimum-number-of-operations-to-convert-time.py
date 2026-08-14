class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        #convert both in minutes
        n1_h = int(current[0:2])
        n1_m = int(current[3:5])

        n2_h = int(correct[0:2])
        n2_m = int(correct[3:5])

        n1_m = n1_m + n1_h*60
        n2_m = n2_m + n2_h*60

        n1_m = n2_m - n1_m
        res = 0

        while n1_m > 0 :
            if n1_m >=60:
                res += 1
                n1_m -= 60
            elif n1_m >= 15:
                res += 1
                n1_m -= 15
            elif n1_m >= 5:
                res += 1
                n1_m -= 5
            else:
                res += 1
                n1_m -= 1
        
        return res

        
        