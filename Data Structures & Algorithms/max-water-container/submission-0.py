class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 1, (2,0) (4,1), (6,4), (7, 2)

        left, right = 0, len(heights) - 1
        result = 0 
        while left < right :
            height = min(heights[left],  heights[right])
            weight = right - left 
            result = max(result, height * weight)

            if heights[left] <= heights[right]:
                left +=1 
            else:
                right -=1 

        return result 
            


            