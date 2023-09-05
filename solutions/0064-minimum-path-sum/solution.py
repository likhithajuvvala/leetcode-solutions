class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[-1 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                    continue
                up=float('inf')
                left=float('inf')
                if i>0:
                    up=grid[i][j]+dp[i-1][j]
                if j>0:
                    left=grid[i][j]+dp[i][j-1]
                dp[i][j]=min(up,left)
        return dp[m-1][n-1]