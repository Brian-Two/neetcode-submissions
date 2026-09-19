import math 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[math.sqrt(point[0]**2 + point[1]**2), point]  for point in points]
        heapq.heapify(points)

        
        closest = []
        for i in range(k):
            closest.append(heapq.heappop(points)[1])
        


        return closest