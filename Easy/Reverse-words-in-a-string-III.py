"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.split()
        l=[]
        for i in x:
            temp=i[::-1]
            l.append(temp)
        s=" "
        s=s.join(l)
        return s            

            