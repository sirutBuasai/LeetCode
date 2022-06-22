class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        dp = [[0 for x in range(col)] for y in range(row)]

        for i in range(row):
          for j in range(col):
            if i == 0 and j == 0:
              dp[i][j] = grid[i][j]

            elif i == 0:
              dp[i][j] = grid[i][j] + dp[i][j-1]

            elif j == 0:
              dp[i][j] = grid[i][j] + dp[i-1][j]

            else:
              dp[i][j] = min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j-1])

        return dp[row-1][col-1]
