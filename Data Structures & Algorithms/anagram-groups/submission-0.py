class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        count = [0] * 26
        anagram_hash = defaultdict(list)

        # iterate through strign list 
        for string in strs:

        # checking the character counts of each letter in the word
            for letter in string:
                count[ord(letter) - ord('a')] += 1 #assume we are only working with lowercase letters

        # if the count is in the hash we append that word to list coresponding to that key 
            
             # if not we intialize a new key with that word
            anagram_hash[tuple(count)].append(string)
            count = [0] * 26
        
        return list(anagram_hash.values())
        
