class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for n in range(k-1):
            heapq.heappop(nums)
        
        return -1 * heapq.heappop(nums)

