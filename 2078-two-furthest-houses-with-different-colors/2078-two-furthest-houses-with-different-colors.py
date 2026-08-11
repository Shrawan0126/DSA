class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i,j = 0, len(colors)-1
        res = 0

        while i < j :
            if colors[i] != colors[j]:
                res = j-i
                break
            else :
                i+=1

        i,j = 0, len(colors)-1

        while i < j :
            if colors[i] != colors[j]:
                res = max(res,j-i)
                break
            else :
                j-=1

        return res