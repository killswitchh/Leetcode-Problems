"""
https://leetcode.com/problems/reverse-string/
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start=0
        endl=len(s)-1
        
        while(start<endl):
            s[start] , s[endl] = s[endl]  , s[start]
            start+=1
            endl-=1
