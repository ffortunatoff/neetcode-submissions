class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        start_color = image[sr][sc]
        def dfs(matrix, r, c, start_color, color):
            ROWS = len(image)
            COLS = len(image[0])

            if min(r,c) < 0 or r == ROWS or c == COLS or image[r][c] == color:
                return image
            elif image[r][c] == start_color:
                image[r][c] = color

                dfs(image,r+1,c,start_color,color)
                dfs(image,r-1,c,start_color,color)
                dfs(image,r,c+1,start_color,color)
                dfs(image,r,c-1,start_color,color)

            return image

        return dfs(image, sr, sc, start_color, color)
