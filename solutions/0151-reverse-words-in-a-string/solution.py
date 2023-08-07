class Solution:
    def reverseWords(self, s: str) -> str:
        lst=s.split()
        lst.reverse()
        x=" ".join(lst)
        return x