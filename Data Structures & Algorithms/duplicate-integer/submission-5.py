class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashdup = {}
        for num in nums:
            if num in hashdup:
                return True
            hashdup[num] = hashdup.get(num, 0) + 1 
        
        return False 
        
