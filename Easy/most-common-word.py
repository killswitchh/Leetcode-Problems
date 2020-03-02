'''
https://leetcode.com/problems/most-common-word/
'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        d={}
        pun=[',','.','!',';','?',"'"]
        for i in pun:
            if(i in paragraph):
                paragraph=paragraph.replace(i," ")
                    
        for i in paragraph.lower().split():
            i=i.replace(" ","")
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        for i in banned:
            if(i in d):
                d[i]=0
        g=max(d.values())
        for i , j in d.items():
            if(j==g):
                return(i)

        
    
        

        
        