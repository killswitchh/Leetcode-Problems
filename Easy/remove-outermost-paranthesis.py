'''
https://leetcode.com/problems/remove-outermost-parentheses/
'''

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count=0
        left=0
        right=0
        g=""
        d={'(':0,')':0}
        for i in S:
            count+=1
            if i in d.keys():
                d[i]+=1
            if (d['(']==d[')']) and d['(']==d[')']!=0:
                right=count
                g+=S[left+1:right-1]
                left=count
        return g
        