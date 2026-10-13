class Solution:
    def romanToInt(self, s: str) -> int:
        rd={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        num=0
        for i in range(len(s)-1):
            if rd[s[i]]<rd[s[i+1]]:
                num-=rd[s[i]]
            else:
                num+=rd[s[i]]
        return num+rd[s[-1]]