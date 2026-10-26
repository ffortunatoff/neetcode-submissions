class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        visited = {}

        def dfs(n):
            if n >= len(cost):
                return 0
            
            if n in visited:
                return visited[n]
                
            visited[n] = cost[n] + min(dfs(n+1),dfs(n+2))
            return visited[n]
        
        return min(dfs(0), dfs(1))