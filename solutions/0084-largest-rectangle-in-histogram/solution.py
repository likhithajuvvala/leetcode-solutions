class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nsr = [0] * n
        nsl = [0] * n

        s = []

        for i in range(n - 1, -1, -1):
            while s and heights[i] <= heights[s[-1]]:
                s.pop()
            if not s:
                nsr[i] = n
            else:
                nsr[i] = s[-1]
            s.append(i)

        while s:
            s.pop()

        for i in range(n):
            while s and heights[i] <= heights[s[-1]]:
                s.pop()
            if not s:
                nsl[i] = -1
            else:
                nsl[i] = s[-1]
            s.append(i)

        ans = 0

        for i in range(n):
            ans = max(ans, heights[i] * (nsr[i] - nsl[i] - 1))
        return ans

        