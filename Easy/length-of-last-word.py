'''
https://leetcode.com/problems/length-of-last-word/
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x=s.split()
        if(len(x)==0):
            return 0
        else:
            ans = len(x[-1])
            return ans
            