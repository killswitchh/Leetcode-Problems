"""
https://leetcode.com/problems/robot-return-to-origin/
"""


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        a=moves.count('L')
        b=moves.count('R')
        c=moves.count('U')
        d=moves.count('D')
        flag=0
        if(a==b):
            flag+=1
            if(c==d):
                flag+=1                    
        if(flag==2):
            return(True)
        else:
            return(False)
        