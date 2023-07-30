class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreater = {}
        
        i = 0
        while i < len(nums2):
            while len(stack) and stack[-1] < nums2[i]:
                k = stack.pop(-1)
                nextGreater[k] = nums2[i]
            stack.append(nums2[i])
            i+=1
        
        while len(stack):
            k = stack.pop(-1)
            nextGreater[k] = -1
        
        result = []
        for i in nums1:
            result.append(nextGreater[i])
        
        return result

       