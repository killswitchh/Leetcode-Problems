'''
https://leetcode.com/problems/implement-strstr/
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(len(needle)==0):
            return 0
        i=0
        j=len(needle)
        while(j<=len(haystack)):
            if(haystack[i:j]==needle):
                return i
            else:
                i+=1
                j+=1
        return -1
        


        