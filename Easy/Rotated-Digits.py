"""
https://leetcode.com/problems/rotated-digits/
"""



class Solution:
    def checkdigits(N):
        #global tes
        d={0:0,1:1,2:5,5:2,6:9,9:6,8:8}
        ht=str(N)
        tex=[i for i in ht]
        t=0
        for i in range(len(tex)):
            
            g=int(tex[i])
            if(g in d.keys()):                
                tex[i] = str(d[g])
                t+=1
        if(len(tex)==t):
            texx="".join(tex)
            if(int(texx)!=N):
            # print(N,texx)
                return(True)        
                
        
    def rotatedDigits(self, N: int) -> int:
        #tes=0
        count=0
        for i in range(1,N+1):
            ans=Solution.checkdigits(i)
            if(ans==True):
                count+=1
                
            
        return(count)