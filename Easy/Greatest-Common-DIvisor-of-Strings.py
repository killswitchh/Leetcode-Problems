"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if(len(str1)>len(str2)):
            ss=str2
        elif(len(str1)   <   len(str2)):
            ss=str1
        else:
            ss=str2
            
        
        right=1
        fin=""
        
        
        while(right<=len(ss)):
            
            text=ss[:right]
            divs=len(str1) // len(text)
            divl=len(str2) // len(text)
            anss=""
            ansl=""
            for i in range(divs):
                anss= anss + text
            for j in range(divl):
                ansl= ansl + text
            if(anss==str1) and (ansl==str2):
                
                if(len(fin)<len(text)):
                    fin=text
            right+=1
            
        return(fin)
            

        
            
            
            
        