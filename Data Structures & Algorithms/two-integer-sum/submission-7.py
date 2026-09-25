class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}
        for i, num in enumerate(nums):
            num_hash[num] = i
        
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in num_hash and i != num_hash[remainder]:
                return([i, num_hash[remainder]])