class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Null check 
        if len(s) != len(t):
            return False

        hash_s = {} # o(26) -> o(1)
        hash_t = {}
        for letter in s: #time o(n)
            hash_s[letter] = hash_s.get(letter, 0) + 1
        for letter in t: # o(n)
            hash_t[letter] = hash_t.get(letter, 0) + 1 
        
        return hash_s == hash_t

        # edge cases: lower/uper case, if we get a non-letter, if we get spaces in between them 