'''
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
'''

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        '''
        working solution with 227 ms runtime
        
        ans=[]
        
        for i in nums:
            count=0
            temp = i
            for j in nums:
                if j < temp:
                    count+=1
            ans.append(count)
        return ans
        
        below is solution learnt from discuss tab
        '''
        
        dic={}
        for i,j in enumerate(sorted(nums)):
            if(j not in dic):
                dic[j]=i
                
        return[dic[i] for i in nums]
