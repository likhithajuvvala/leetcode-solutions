class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count=Counter(s)
        visited=set()
        stack=[]
        for i in s:
            count[i]-=1
            if i in visited:
                continue
            while stack and stack[-1]>i and count[stack[-1]]:
                visited.remove(stack.pop())
            stack.append(i)
            visited.add(i)
        return"".join(stack)
       