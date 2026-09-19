class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # remainders = {}
        # for i in range(len(nums)):
        #     remainders[target-nums[i]] = i 
        
        # for i in range(len(nums)):
        #     curr = nums[i]
        #     if curr in remainders and i != remainders[curr]:
        #         return [i, remainders[curr]]

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i 
            