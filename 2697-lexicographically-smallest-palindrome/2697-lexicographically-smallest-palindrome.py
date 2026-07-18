class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        temp = list(s)
        i = 0
        j = len(temp) - 1
        
        while i < j:
            if temp[i] != temp[j]:
                temp[i] = temp[j] = min(temp[i], temp[j])
            i += 1
            j -= 1
            
        return "".join(temp)
