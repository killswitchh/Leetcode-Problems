'''
https://leetcode.com/problems/count-and-say/
'''

class Solution:
    def countAndSay(self, n: int) -> str:
        dp = ['']*32
        dp[1] = '1'
        dp[2] = '11'
        for i in range(3, n+1):
            count = 0
            l = len(dp[i-1])
            s = dp[i-1]
            for j in range(l):
                count += 1
                if(j+1 < l and s[j]!=s[j+1]):
                    dp[i] = dp[i] + str(count) + s[j]
                    count = 0
            dp[i] = dp[i] + str(count) + s[j]
            count = 0
        return dp[n]