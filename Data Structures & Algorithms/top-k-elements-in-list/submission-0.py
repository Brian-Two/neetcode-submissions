class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counthash = {}
        for num in nums:
            counthash[num] = counthash.get(num, 0) + 1
        
        bucket= [] # index refers to frequency 
        for count, freq in counthash.items():
            heapq.heappush(bucket, (freq, count))
            if len(bucket) > k:
                heapq.heappop(bucket)
        topk = []

        for i in range(k):
            topk.append(heapq.heappop(bucket)[1])

        return topk