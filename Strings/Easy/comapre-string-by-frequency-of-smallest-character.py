'''
https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
'''
class Solution:
   
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        from collections import Counter
        l=[]
        u=[]
        for i in queries:
            x=[j for j in i]
            l.append(x)
        
        for i in words:
            y=[k for k in i]
            u.append(y)
        a1=[]
        a2=[]
        for i in l:
            a=Counter(i)        
            y=max(a.values())
            a1.append(y)
            
        for j in u:
            b=Counter(j)
            z=max(b.values())
            a2.append(z)
            
        print(a1,a2)  
            
        
        
        
            