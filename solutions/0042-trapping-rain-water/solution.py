class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        leftmax=height[left]
        rightmax=height[right]
        res=0
        while(left<=right):
            leftmax,rightmax=max(leftmax,height[left]),max(rightmax,height[right])
            if(leftmax<=rightmax):
                res+=leftmax-height[left]
                left+=1
            else:
                res+=rightmax-height[right]
                right-=1
        return res

        
