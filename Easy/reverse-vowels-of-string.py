'''
https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        li,i,j,v = list(s),0,len(s)-1,set('aeiouAEIOU')
        while i<j:
            
            if li[i] in v and li[j] in v:
                li[i] ,li[j] = li[j],li[i] 
                i,j = i+1,j-1
                continue            
            if li[i] not in v : i+=1
            if li[j] not in v : j-=1
        return ''.join(li)