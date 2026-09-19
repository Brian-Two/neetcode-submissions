class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numhash = {}
        for num in nums:
            numhash[num] = numhash.get(num, 0 ) + 1

        bucket = [] # (freq, elm)
        for num, freq in numhash.items():
            heapq.heappush(bucket, (freq, num))
            if len(bucket) > k:
                heapq.heappop(bucket)
        
        res= []
        print(bucket)
        for i in bucket:
            res.append(i[1])
        return res
        



        