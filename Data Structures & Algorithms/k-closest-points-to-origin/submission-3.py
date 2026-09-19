import math 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[math.sqrt(point[0]**2 + point[1]**2), point]  for point in points]
        print(points)
        heapq.heapify(points)
        print(points)

        
        closest = []
        for i in range(k):
            closest.append(heapq.heappop(points)[1])
        
        print(closest)


        return closest