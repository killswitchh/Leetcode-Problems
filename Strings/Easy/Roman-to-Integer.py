"""
https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman={'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000 }
        x=[roman[i] for i in s]
        ans=0
        for i in range(len(x)-1):
            if(x[i]<x[i+1]):
                ans-=x[i]
            else:
                ans+=x[i]
        ans+=x[-1]
        return(ans)
        
                