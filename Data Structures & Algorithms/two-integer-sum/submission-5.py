class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = {}

        for i in range(len(nums)):
            remainders[target - nums[i]] = i 
        for i in range(len(nums)):
            if nums[i] in remainders and remainders[nums[i]] != i:
                return [i, remainders[nums[i]]]
        print(remainders)
