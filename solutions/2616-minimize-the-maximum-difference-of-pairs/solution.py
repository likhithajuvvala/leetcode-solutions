class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        
        def search(target: int) -> int:
            total, i = 0, 1
            while i < n:
                if nums[i] - nums[i-1] <= target:
                    total += 1
                    i += 2
                else:
                    i += 1
            return total
        
        l, r = 0, nums[n-1] - nums[0]
        while l < r:
            m = l + (r - l) // 2
            total = search(m)
            if total < p:
                l = m + 1
            else:
                r = m
        return l