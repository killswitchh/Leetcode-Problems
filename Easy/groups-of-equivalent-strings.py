'''
https://leetcode.com/problems/groups-of-special-equivalent-strings/
'''

from collections import Counter
class Solution:
    def doo(x):
        return tuple(sorted(x.items()))
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        B=set()
        for word in A:
            odd=Counter(word[::2])
            even=Counter(word[1::2])
            odd=Solution.doo(odd)
            even=Solution.doo(even)
            B.add((odd,even))
        return(len(B))
            
            