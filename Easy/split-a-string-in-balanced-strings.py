'''
https://leetcode.com/problems/split-a-string-in-balanced-strings/
'''
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left=0
        right=0
        d={'L':0,'R':0}
        count=0

        while(right<len(s)):

            #print(loop,left,right)
            if(s[right]=='R'):
                d['R']+=1
            if(s[right]=='L'):
                d['L']+=1
            #print(d)
            if(d['L']==d['R'] and d['L']!=0 and d['R']!=0):
                count+=1
                #print("condition matched",l)
                left=right+1
                d['L']=0
                d['R']=0
                #print("dict reset",d)
            right+=1
        return count