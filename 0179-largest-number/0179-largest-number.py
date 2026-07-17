class Solution:
    from functools import cmp_to_key
    def largestNumber(self, nums: List[int]) -> str:
        arr = list(map(str,nums))
        
        arr.sort(
            key=cmp_to_key(
                lambda a,b : -1 if a+b > b+a else (1 if a+b < b+a else 0)
            )
        )

        return "0" if arr[0] == "0" else "".join(arr)