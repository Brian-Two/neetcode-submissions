class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, window = 0, 0, 0 
        min_sub = float('inf')
        while r < len(nums):
            window += nums[r]
            while window >= target:

                min_sub = min(min_sub, r- l + 1) 
                window -= nums[l]
                l +=1
            r +=1


        return 0 if min_sub == float('inf') else min_sub 
