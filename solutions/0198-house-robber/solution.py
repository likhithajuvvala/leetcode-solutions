class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        dp[0]=nums[0]
        for i in range(1,n):
            pick=nums[i]
            if i>1:
                pick+=dp[i-2]
            non_pick=dp[i-1]
            dp[i]=max(pick,non_pick)
        return dp[n-1]
