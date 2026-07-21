class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        seats.sort()

        res = 0

        for i in range(0, len(seats)):
            res = res + abs(seats[i] - students[i])

        return res