class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited=set()
        for i in nums:
            if i not in visited:
                visited.add(i)
            else:
                return i