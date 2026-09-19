class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #two pointer approach where we reutrn the left pointer 
        n = len(nums)
        uni = 1 
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[uni] = nums[i] 
                uni +=1
        return uni 
                
        