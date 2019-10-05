'''
https://leetcode.com/problems/longest-common-prefix/
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs)==0):
            return ""
        minn=111111111111
        for i in strs:
            if(len(i)<minn):
                minn=len(i)
                x=i
        left=0
        right=1
        ans=""
        while(right<=minn):
            count=0
            window = x[left:right]
            for i in strs:
                if(window==i[left:right]):
                    count+=1
            if(count==len(strs)):
                ans=window
            right+=1
        return(ans)

        