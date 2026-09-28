class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) -1 
        res = (r-l) * min(heights[l], heights[r])
        # print(f"res:{res}")
        while l < r:
            curr = (r-l) * min(heights[l], heights[r])
            if heights[l]< heights[r]:
                l +=1
            else:
                r-=1
            # print(f"curr:{curr}")

            res = max(res, curr)

        # print(f"final-res:{res}")

        return res 
