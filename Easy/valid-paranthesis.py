'''
https://leetcode.com/problems/valid-parentheses/
'''


class Solution:
    def isValid(self, s: str) -> bool:
        d={'(':')' , '{':'}' , '[':']'}
        stack=[]
        if(len(s)==1):
            return False
        if(len(s)==0):
            return True
        
        for i in s:
            if(i in d.keys()):
                
                stack.append(i)
            elif(len(stack)==0 and i in d.values()):
                return(False)

            elif(d[stack[-1]]==i):
                stack = stack[:-1]
            else:
                return False
        if(len(stack)==0):
            return True
                