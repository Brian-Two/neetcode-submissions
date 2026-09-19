class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasseen = set()
        for num in nums:
            if num in hasseen:
                return True 
            hasseen.add(num)
        
        return False