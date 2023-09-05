class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        prev=[0]*n
        for i in range(m):
            cur=[0]*n
            for j in range(n):
                if i==0 and j==0:
                    cur[j]=grid[i][j]
                    continue
                up=float('inf')
                left=float('inf')
                if i>0:
                    up=grid[i][j]+prev[j]
                if j>0:
                    left=grid[i][j]+cur[j-1]
                cur[j]=min(up,left)
            prev=cur
        return prev[n-1]