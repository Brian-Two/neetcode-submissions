class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # window = []
        # longest_sub = 0
        # for letter in s:
        #     if letter not in window:
        #         window.append(letter)

        #     elif letter in window:
        #         longest_sub = max(longest_sub, len(window))
        #         window = [letter]


        # return longest_sub

        seen = set()
        left  = 0 
        longest_sub = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left +=1
            seen.add(s[right])
            longest_sub = max(longest_sub, right - left +1)

        return longest_sub 
            
