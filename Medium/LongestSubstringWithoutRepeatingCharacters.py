"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        n=len(s)
        l=[]
        max=0
        while(right < len(s)):
            if(s[right] not in l):
                l.append(s[right])
                right+=1
                if(len(l)>max):
                    max=len(l)
               
            else:
                l.pop(0)
                left+=1
        return(max)