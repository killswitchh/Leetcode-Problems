'''
https://leetcode.com/problems/longest-palindromic-substring/
'''
class Solution:
    def reversee(S):
        if(S==S[::-1]):
            return True
        else:
            return False
    def longestPalindrome(self, s: str) -> str:
        anss=''
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                temp=s[i:j]
                ans=Solution.reversee(temp)
                #print(temp,ans)
                if(ans==True) and (len(anss)<len(temp)):
                    anss=temp
        return(anss)
                
                    