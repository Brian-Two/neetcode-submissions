class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if s == "":
        #     return 0 
        # length = 1
        # l = 0 
        # for i in range(len(s)):
        #     while s[i] in s[l:i]:
        #         l+=1
        #     length = max(length, len(s[l:i+1]))
        
        # return length 
        
        mp  = {}
        l = 0 
        res = 0 

        for i in range(len(s)):
            
            if s[i] in mp:
                l = max(mp[s[i]] + 1, l)
            mp[s[i]] = i 
            res = max(res, i-l+1)
        return res
            

