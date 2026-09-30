class Solution:
    def climbStairs(self, n: int) -> int:
        visited = {}

        def dfs(n):
            if n <= 2:
                return n

            if n in visited:
                return visited[n]

            visited[n] = dfs(n - 1) + dfs(n - 2)
            return visited[n]

        return dfs(n)


        
