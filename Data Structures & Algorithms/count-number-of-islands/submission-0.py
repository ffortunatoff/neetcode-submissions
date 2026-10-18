class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0

        def dfs(r, c):
            # base case
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == '0':
                return 0

            # mark visited   
            grid[r][c] = '0'

            # check neighbors
            neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
            for nr, nc in neighbors:
                dfs(r+nr, c+nc)

            return 1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    res += dfs(i, j)

        return res


