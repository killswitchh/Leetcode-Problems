"""
https://leetcode.com/problems/unique-email-addresses/
"""
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans=set()
        for email in emails:
            k=email.split('@')
            ename=k[1]
            if('+' in k[0]):                
                temp=list(k[0])
                ind=temp.index('+')
                lname=temp[0:ind]
                lname=''.join(lname)            
            else:
                lname=k[0]
            if('.' in lname):
                lname=lname.replace('.','')
                
            full=lname+'@'+ename
            ans.add(full)
        #print(ans)
        return(len(ans))
            