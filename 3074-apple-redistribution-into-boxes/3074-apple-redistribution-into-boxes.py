class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        res = 0
        count = 0
        for ca in capacity:
            res += ca
            count+=1
            if res >= total : break

        return count