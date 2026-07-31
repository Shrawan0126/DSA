class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word).most_common()
        res = 0

        for i in range(0,len(freq)):
            if i < 8:
                res += 1*freq[i][1]
            elif i < 16:
                res += 2*freq[i][1]
            elif i < 24:
                res += 3*freq[i][1]
            else :
                res += 4*freq[i][1]
        
        return res