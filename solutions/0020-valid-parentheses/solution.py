class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i in "([{":
                st.append(i)
            else:
                if i==')':
                    if len(st)>0:
                        p=st.pop()
                        if p=="{" or p=="[":
                            return False
                    else:
                        return False
                elif i=="]":
                    if len(st)>0:
                        p=st.pop()
                        if p=="{" or p=="(":
                            return False
                    else:
                        return False
                elif i=="}":
                    if len(st)>0:
                        p=st.pop()
                        if p=="(" or p=="[":
                            return False
                    else:
                        return False
        return True if len(st)==0 else False
                    
                
