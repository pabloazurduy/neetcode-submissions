class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        visited:List[int] = []

        def dfs(i:int) -> None:
            nonlocal visited
            visited.append(i)
            
            neighboors:List[int] = []
            for e in edges:
                if i in e and sum(e)-i not in visited:
                    #dges.remove(e)
                    neighboors.append(sum(e)-i)

            if len(neighboors) == 0:
                return 

            for j in neighboors:
                dfs(j)


        nodes = list(range(n))
        components = 0
        while len(visited) < len(nodes):
            for i in nodes:
                if i not in visited:
                    dfs(i)
                    components+=1

        return components