'''
https://leetcode.com/problems/self-dividing-numbers/
'''

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l=[]
        ans=[]
        for i in range(left,right+1):
            g=str(i)
            if('0' not in g):
                l.append(i)
        for j in l:
            count=0
            v=str(j)
            for k in v:
                if(j % int(k) ==0):
                    count+=1
            if count == len(v):
                ans.append(j)
        return(ans)    
           
                    