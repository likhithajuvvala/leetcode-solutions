class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        dp=[[0]*len(g[0]) for i in range(len(g))]
        if g[0][0]==0:
            dp[0][0]=1
        for i in range(1,len(g[0])):
            if g[0][i]==0:
                dp[0][i]=dp[0][i-1]
        for i in range(1,len(g)):
            if g[i][0]==0:
                dp[i][0]=dp[i-1][0]
        for i in range(1,len(g)):
            for j in range(1,len(g[0])):
                if g[i][j]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
        