class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW_NUM = len(grid)
        COL_NUM = len(grid[0])

        max_area = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROW_NUM or c >= COL_NUM or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0 # mark as visited

            area = 1

            neighbors = [[0,1],[1,0],[0,-1],[-1,0]]
            for nr, nc in neighbors:
                area += dfs(r + nr, c + nc)

            return area

        for r in range(ROW_NUM):
            for c in range(COL_NUM):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area