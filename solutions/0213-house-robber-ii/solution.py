class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        def helper(nums):
            prev, curr = 0, 0
            for n in nums:
                prev, curr = curr, max(n + prev, curr)
            return curr

        return max(helper(nums[1:]), helper(nums[:-1]))
        