class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        
        if n <= 8:
            return n
        elif n >= 9 and n <= 16:
            return 8 + (n-8)*2
        elif n >= 17 and n <= 24:
            return 8 + 16 + (n-16)*3
        else :
            return 8 + 16 + 24 + (n-24)*4
