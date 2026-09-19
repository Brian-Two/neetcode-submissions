class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # search te 2^d array -> if we hit a 1 then we do a dfs for that 1 and include that 1 + connecting 1s to seen

        islands = 0 
        rows, cols = len(grid), len(grid[0])
        seen = set() # (row,col)

        def dfs(row, col):
            # base case 
            if row >= rows or row < 0 or col >= cols or col < 0:
                return  
            if grid[row][col] == '0' or (row, col) in seen:
                return

            seen.add((row, col))
            #iterative case
            dfs(row, col+1)
            dfs(row, col-1)
            dfs(row+1, col)
            dfs(row-1, col)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row,col) not in seen:
                    islands +=1
                    dfs(row, col)
        

        return islands       