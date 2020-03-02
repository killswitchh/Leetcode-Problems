"""
https://leetcode.com/problems/detect-capital/
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap=0
        sma=0
        jinx=0
        
        for i in word:
            if (i.isupper()):
                cap+=1
            else:
                sma+=1
        if( word[0].isupper() ) and (sma==len(word)-1):
            jinx=69
            
            
           
        if(sma==len(word)) or (cap==len(word)) or(jinx==69):
            return(True)
        else:
            return(False)
                
            
        
        
                
                    
            
        