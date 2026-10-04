class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        start_color = image[sr][sc]
        if start_color == color:
            return image

        ROWS = len(image)
        COLS = len(image[0])

        def dfs(r, c):
            if min(r,c) < 0 or r == ROWS or c == COLS or image[r][c] != start_color:
                return

            image[r][c] = color

            neighbors = [[0,1], [0,-1], [1,0], [-1,0]]
            for nr,nc in neighbors:
                dfs(r+nr,c+nc)

        dfs(sr, sc)
        return image
