'''
https://leetcode.com/problems/container-with-most-water/
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if(len(height)==0):
            return 0
        maxx=0
        left =  0
        right = len(height)-1
        
        
        while(left<right):
            length = right-left
            breadth = min(height[right],height[left])
            
            area = length * breadth
            if(area>maxx):
                maxx=area
            
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return maxx
        
            
        