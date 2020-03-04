'''
https://leetcode.com/problems/add-digits/submissions/
'''
class Solution:
    '''
    32 ms runtime
    def action(num):
        sum=0
        while(num>0):
            temp = num%10
            sum+=temp
            num=num//10
        return sum
    
    def addDigits(self, num: int) -> int:
        ans=num
        while(len(str(ans))!=1):
            num=ans
            ans=Solution.action(num)
        return ans

    Below is 24 ms runtime solution.
    '''
    def addDigits(self, num: int) -> int:
        if (num==0):
            return num
        else:
            return num%9 or 9