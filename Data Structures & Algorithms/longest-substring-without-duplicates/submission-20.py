class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0 
        length = 1
    
        l = 0 
        #'au'| i  = 0 s[i] = a s[l:i] = a length  = 0 | i = 1, s[i] = u s[l:i] = au

        for i in range(len(s)):
        
            while s[i] in s[l:i]:
                l+=1
            
            

            length = max(length, len(s[l:i+1]))
            
            
        
        return length 
            