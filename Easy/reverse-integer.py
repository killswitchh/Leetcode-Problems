'''
https://leetcode.com/problems/reverse-integer/
'''

class Solution:
    def removezero(s):
        temp=''
        if(s[0]=='-'):
            temp=s[:1]
            s=s[1:]
        s=s.strip('0')
        s=s[::-1]
        if(temp):
            s=temp+s
        if  int(s)<=2147483647 and int(s)>= -2147483647:
            return (int(s))
        else:
            return 0
    def reverse(self, x: int) -> int:
        num= str(x)
        if(num[0]=='0'):
            count=0
            i=0
            while(num[i]==0):
                i+=1
                count+=1
            if(count==len(num)-1):
                return int(num)
                
        if(num[0]!='-'):
            ans=Solution.removezero(num)
            return ans
        
        if(num[0]=='-'):
            ans=Solution.removezero(num)
            return ans