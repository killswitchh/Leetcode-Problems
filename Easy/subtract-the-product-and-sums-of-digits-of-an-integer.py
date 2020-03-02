'''
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
'''

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ=0
        prod=1
        for i in str(n):
            i=int(i)
            summ+=i
            prod*=i
        return prod-summ
        
        