class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        sorted_counts = Counter(s).most_common()[::-1]

        if len(sorted_counts) <= k:
            return 0

        res = 0

        for i in range(0,len(sorted_counts)-k):
            res += sorted_counts[i][1]

        return res

