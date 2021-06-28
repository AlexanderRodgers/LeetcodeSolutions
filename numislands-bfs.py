class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])

        q = []

        def bfs(r, c):
            q.append((r, c))
            while q:
                r, c = q.pop()
                if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
                    continue
                grid[r][c] = "0"
                q.append(r + 1, c)
                q.append(r - 1, c)
                q.append(r, c + 1)
                q.append(r, c - 1)
            
        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)
        return count