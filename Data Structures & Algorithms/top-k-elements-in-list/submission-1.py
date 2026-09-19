class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counthash = {}
        for num in nums:
            counthash[num] = counthash.get(num, 0) + 1
        bucket = []
        for num, freq in counthash.items():
            heapq.heappush(bucket, (freq, num))  
            if len(bucket) > k:
                heapq.heappop(bucket)
        res = []
        for i in range(k):
            res.append(heapq.heappop(bucket)[1])

        return res