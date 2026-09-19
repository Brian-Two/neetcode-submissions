class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
    
        for s in strs:
            count = [0] * 26 
            for c in s:
                count[ord(c) - ord("a")] +=1
        
            ans[tuple(count)].append(s)
        return list(ans.values())
        # some type of hashmap to see the set of letters and every word that fits in there like:
        # hash = {
        # ('a','c','t'): ["act", "cat"]
        # ('p', 'o', 't', 's'): ["stop", "pots", "tops"] }

        # to make this hash we have to:
        # 1. go through each string in strs
        # 2.  for each strin in str:
                # check if the set of the strign is already in the hash if not make that strign the first in that list, if it is then add it ot that list

        # anagrams_hash = {}

        # for word in strs:
        #     key = tuple(sorted(word))
        #     if key in anagrams_hash:
        #         anagrams_hash[key].append(word)
        #     else:
        #         anagrams_hash[key] = [word]
        #     # anagrams_hash[tuple(word)] = anagrams_hash.get(tuple(word), []).append(word)

        # print(anagrams_hash)


        
        # #then return a list of each value in the hash 

        # # res  = []
        # # for key, value in anagrams_hash.items():
        # #     res.append(value)
        # # return res 

        # return list(anagrams_hash.values())

        # time - o(n * klogk): n is the number of strings, k is the avg string length 
        # space - o(n)


