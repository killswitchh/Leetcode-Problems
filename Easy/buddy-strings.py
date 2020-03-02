'''
https://leetcode.com/problems/buddy-strings/
'''
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        if(len(A)!=len(B)):
            return False       
        if(A==B):
            return len(A) > len(set(A))
        else:
            l=[]          
            for i,j in zip(A,B):
                if(i!=j):
                    l.append((i,j))               
                if(len(l)>2):
                    return False             
            return len(l)==2 and l[0] == l[1][::-1]
            