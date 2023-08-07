class Solution:
    def isThree(self, n: int) -> bool:
        cnt=2
        for i in range(2,n//2+1):
            if n%i==0:
                cnt+=1
            if cnt>3:
                return 0
        if cnt!=3:
            return 0
        return 1
        