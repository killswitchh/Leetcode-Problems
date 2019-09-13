"""
https://leetcode.com/problems/first-unique-character-in-a-string/
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if(s==""):
            return -1
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        #print(d)
        flag=0
        for i,j in d.items():
            if(j==1):
                flag=1
                return(s.index(i))
        if(flag==0):
            return(-1)
                

    
            
        