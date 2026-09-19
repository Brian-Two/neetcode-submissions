class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for x in range(len(stones)):
            stones[x] *= -1
            
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones) 
            stone2 = heapq.heappop(stones) 
        
            if stone1 < stone2:
                heapq.heappush(stones, stone1 - stone2)
        
        return stones[0] * -1 if stones else 0

        