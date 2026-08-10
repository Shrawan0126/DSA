class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0

        for j in range(0,m):
            for i in range(0,n-1):
                if grid[i][j] >= grid[i+1][j]:
                    res = res + grid[i][j] - grid[i+1][j] + 1
                    grid[i+1][j] += grid[i][j] - grid[i+1][j] + 1

        return res
