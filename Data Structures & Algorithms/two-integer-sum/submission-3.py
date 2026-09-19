class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #using two pointers since it is already ordered 
        # nums = [(num, i ) for i, num in enumerate(nums)]
        
        # nums.sort() #o(n log n)

        # left, right = 0, len(nums) - 1

        # while left < right:
        #     current_sum = nums[left][0] + nums[right][0]


        #     if current_sum == target:
        #         return [nums[left][1], nums[right][1]]
        #     elif current_sum < target:
        #         left += 1
        #     else:
        #         right -= 1
        
      
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i