'''
https://leetcode.com/problems/decompress-run-length-encoded-list/
'''
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        '''
        better than 42% runtime
        
        ans=[]
        while(len(nums)!=0):
            arr=nums[:2]
            for i in range(arr[0]):
                ans.append(arr[1])
            nums=nums[2:]
        return ans
        
        SOLUTION 2
        
        res=[]
        for i in range(1,len(nums),2):
            ans=[nums[i]]*nums[i-1]
            res.extend(ans)
        return res
        '''
        
        return sum( [ [nums[i+1]] * nums[i]  for i in range(0,len(nums),2)],[] )