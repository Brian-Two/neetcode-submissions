class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        #slide a window through the array
        for num in nums:
            currSum = max(currSum, 0)
            currSum += num 
            maxSum = max(maxSum, currSum)

        # keep track of every window 

        # if we get to a postiton that brings that window negative we reset the widnow

        return maxSum