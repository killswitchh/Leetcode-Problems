'''
https://leetcode.com/problems/jewels-and-stones/
'''
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels=list(J)
        sum=0
        for jewel in jewels:
            if jewel in S:
                sum+=S.count(jewel)
        return sum