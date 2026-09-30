class Solution:
    def findMin(self, nums: List[int]) -> int:
        # minimun = nums[0]
        # for n in nums:
        #     minimun = min(minimun, n)
        # return minimun
        low = 0 
        high = len(nums) -1
        #nums=[3,4,5,6,1,2]
        # low
        
        while low < high:
            mid = low + (high-low)//2
            if nums[mid] > nums[high]:
                low = mid +1
            else:
                high = mid
            mid = low + (high-low)//2

        return nums[low]




