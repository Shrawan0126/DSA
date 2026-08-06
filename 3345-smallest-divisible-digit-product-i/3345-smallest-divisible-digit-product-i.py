class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while True:
            prod = math.prod(int(d) for d in str(n))
            if prod % t == 0 :
                return n
            n+=1

        return -1