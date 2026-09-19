class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
           # hashdup = {}
        # for num in nums:
        #     if num in hashdup:
        #         return True
        #     hashdup[num] = hashdup.get(num, 0) + 1 
        
        # return False 
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
        