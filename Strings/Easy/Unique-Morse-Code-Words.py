"""
https://leetcode.com/problems/unique-morse-code-words/
"""



class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dic=        {
            'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.',
             'h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.',
             'o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-',
             'v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..'
        }
        
       
        ans=set()
        for word in words:
            a=""
            for letter in word:
                a+=dic[letter]
            ans.add(a)
        return(len(ans))
            
