class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dup = {}

        for i in range(len(nums)):
            
            remainder = target - nums[i]
            print(dup)
            if remainder in dup:
                return [dup[remainder], i]
            dup[nums[i]] = i 

        