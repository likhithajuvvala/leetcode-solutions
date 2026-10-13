class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        for i in range(len(s)):
            if s[i]=="(":
                st.append(s[i])
            else:
                if len(st)>0 and st[-1]=="(":
                    st.pop()
                else:
                    st.append(s[i])
        return len(st)