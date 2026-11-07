class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        color = ["w" for _ in range(n)]
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(i):
            color[i] = "g"

            for nei in adj[i]:
                if color[nei] == "w":
                    dfs(nei)
            color[i] = "b"
        
        count = 0
        for i in range(n):
            if color[i] == "w":
                dfs(i)
                count += 1
        
        return count
                

        
        