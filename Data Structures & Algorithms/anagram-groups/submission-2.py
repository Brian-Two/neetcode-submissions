class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)


        for s in strs:
            count = [0] * 26 
            for letter in s:
                place = ord(letter) - ord('a')
                count[place] +=1

            res[tuple(count)].append(s)

        return list(res.values())

