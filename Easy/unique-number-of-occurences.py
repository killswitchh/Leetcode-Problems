'''
https://leetcode.com/problems/unique-number-of-occurrences/
'''
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        
        for i in arr:
            if(i in d):
                d[i]+=1
            else:
                d[i] = 1
        b=len(d.values())
        a=len(set(d.values()))
        if(b==a):
            return True
        else:
            return False

