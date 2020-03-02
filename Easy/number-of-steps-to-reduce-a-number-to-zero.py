'''
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
'''

class Solution:
    def numberOfSteps (self, num: int) -> int:
        '''
        84% better runtime solution
        
        count=0
        while(num!=0):
            count+=1
            if num%2==0:
                num=num//2
                
            else:
                num=num-1
                
        return count
        '''
        
        count=0
        while(num>0):
            if(num%2==0) or (num==1):
                count+=1
            else:
                count+=2
            num = num//2
        return count