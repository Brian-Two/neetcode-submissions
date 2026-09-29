class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        l,r = 0,0
        window_freq = {}
        #s = "XYYX", k = 2 frq
        #.    lr
        while r < len(s):
            window_freq[s[r]] = window_freq.get(s[r], 0) + 1
            highest_freq = max(window_freq.values())
            window = r-l +1
            if window - highest_freq <= k:
                res = max(res, window)
            else:
                window_freq[s[l]] -=1
                l +=1
            r+=1
        return res 




