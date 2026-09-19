class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Null check 
        if len(s) != len(t):
            return False

        hash_s = {}
        hash_t = {}
        for letter in s:
            hash_s[letter] = hash_s.get(letter, 0) + 1
        for letter in t:
            hash_t[letter] = hash_t.get(letter, 0) + 1 
        
        return hash_s == hash_t