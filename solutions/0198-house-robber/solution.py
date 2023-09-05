class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(ind,nums):
            if ind==0:
                return nums[ind]
            if ind<0:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            pick=nums[ind]+solve(ind-2,nums)
            not_pick=0+solve(ind-1,nums)
            dp[ind]= max(pick,not_pick)
            return dp[ind]
        n=len(nums)
        dp=[-1]*n
        return solve(len(nums)-1,nums)