"""
https://leetcode.com/problems/goat-latin/

"""


class Solution:
    
    def toGoatLatin(self, S: str) -> str:
        x=S.split()
        v=['a','e','i','o','u','A','E','I','O','U']
        for i in range(len(x)):
            temp=""
            for j in range(i+1):
                    temp=temp+'a'
                
            if(x[i][0] in v):
                
                x[i]=x[i]+'ma'
                x[i]=x[i] + temp + ' '
                
            else:
                x[i]=x[i][1:] + x[i][0] + 'ma'
                x[i]=x[i]  + temp +' '
        ans=""
        ans=ans.join(x)
        return(ans[:len(ans)-1])
                
        