class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj:List[List[int]] = [[] for _ in range(n)] # adj[i] will have all the neighboors of i 
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited:List[int] = []


        def dfs(i:int) -> None:
            nonlocal visited
            visited.append(i)
            
            for j in adj[i]:
                if j not in visited:
                    dfs(j)


        nodes = list(range(n))
        components = 0
       
        for i in nodes:
            if i not in visited:
                dfs(i)
                components+=1

        return components