class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nrs = [0] * n
        nls = [0] * n

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if not stack:
                nrs[i] = n
            else:
                nrs[i] = stack[-1]
            stack.append(i)

        while stack:
            stack.pop()

        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if not stack:
                nls[i] = -1
            else:
                nls[i] = stack[-1]
            stack.append(i)

        ans = 0

        for i in range(n):
            ans = max(ans, heights[i] * (nrs[i] - nls[i] -1))
        return ans

        