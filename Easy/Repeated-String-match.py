"""
https://leetcode.com/problems/repeated-string-match/
"""
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        count=1
        flag=0
        temp=A
        while(flag!=1):
            if(B in temp):
                flag=1            
                break
            temp+=A
            count+=1
            if(len(temp)>10000):
                count=-1
                break
        return(count)
        