class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = "".join(s.split())    
        t_list = "".join(t.split())    

        hash_s = {}
        hash_t = {}
    
        for i in range(len(t)):
            hash_s[s_list[i]] = hash_s.get(s_list[i], 0 ) + 1
            hash_t[t_list[i]] = hash_t.get(t_list[i], 0 ) + 1

        return (hash_s == hash_t)

        

        
