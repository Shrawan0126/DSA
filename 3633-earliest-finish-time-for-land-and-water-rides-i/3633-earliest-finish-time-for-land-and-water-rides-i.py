class Solution:
    def find_finish_time(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]):
        n = len(landStartTime)
        m = len(waterStartTime)
        mini = float('inf')   # Infinity

        for i in range(n):
            mini = min(mini, landStartTime[i] + landDuration[i])

        ans = float('inf')

        for i in range(m):
            actual_finish = max(mini, waterStartTime[i]) + waterDuration[i]
            ans = min(ans, actual_finish)

        return ans

    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        return min(
            self.find_finish_time(landStartTime,landDuration,waterStartTime,waterDuration),
            self.find_finish_time(waterStartTime,waterDuration,landStartTime,landDuration)
        )