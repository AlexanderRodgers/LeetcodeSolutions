class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        R, C = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count