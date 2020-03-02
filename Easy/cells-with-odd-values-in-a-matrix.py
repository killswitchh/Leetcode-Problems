'''
https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
'''

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        a=[]    
        for i in range(n):
            b=[]
            for j in range(m):
                b.append(0)
            a.append(b)
        for i in indices:
            left=i[0]
            right=i[1]
            for k in range(n):
                for l in range(m):
                    if(k==left):
                        a[k][l]+=1
                    if(l==right):
                        a[k][l]+=1
        ans=0
        for i in a:
            for j in i:
                if(j%2!=0):
                    ans+=1
        return ans
                
