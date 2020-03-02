"""
https://leetcode.com/problems/defanging-an-ip-address/
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans=address.replace('.','[.]')
        return(ans)
                