"""
https://leetcode.com/problems/reverse-only-letters/
"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        l=[x for x in S]
        a=[]
        for i in S:
            if(i.isalpha()==True):
                a.append(i)
        g=a[::-1]
        j=0
        for i in range(len(l)):
            if(l[i].isalpha()==True):
                #print(g[j])
                l[i]=g[j] 
                j=j+1
        ans=''.join(l)
        return(ans)
                