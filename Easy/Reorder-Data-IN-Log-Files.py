
"""
https://leetcode.com/problems/reorder-data-in-log-files/
"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        ans1=[]
        ans2=[]
        for i in logs:
            x=i.split()
            #print(x)
            item = x[1]
            #print(item)
            for j in item:
                if(j.isalpha()==True):
                    flag=1                    
                elif(j.isnumeric()==True):
                    flag=2
            if(flag==1):
                ans1.append(i)
            elif(flag==2):
                ans2.append(i)
        #print(ans1)
        #print(ans2)
        ans1=sorted(ans1,key= lambda x : (x.split(" ")[1::] , x.split(" ")[0])  )
        return(ans1 + ans2)
        
                
        