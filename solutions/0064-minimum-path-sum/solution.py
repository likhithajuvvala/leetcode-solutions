class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def solve(i:int,j:int)->int:
            if i==0 and j==0:
                return grid[0][0]
            if i<0 or j<0:
                return 1e9
            if dp[i][j]!=-1:
                return dp[i][j]
            up=grid[i][j]+solve(i-1,j)
            left=grid[i][j]+solve(i,j-1)
            dp[i][j]= min(up,left)
            return dp[i][j]
        m,n=len(grid),len(grid[0])
        dp=[[-1 for j in range(n)] for i in range(m)]
        return solve(m-1,n-1)
