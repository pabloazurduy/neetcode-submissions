from itertools import product

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        to_visit = set(product(range(len(grid)), range(len(grid[0]))))

        def dfs(i:int, j:int) -> int:

            if grid[i][j]==0:
                return 0
            
            areas = []
            for u,v in [(1,0),(0,1),(-1,0),(0,-1)]: 
                if (i+u,j+v) in to_visit:
                    to_visit.remove((i+u,j+v))
                    areas.append(dfs(i+u, j+v))

            return 1+ sum(areas)


        largest = 0
        
        while to_visit:
            (i,j) = to_visit.pop()
            if grid[i][j]==1:
                print("call")
                largest = max(largest, dfs(i,j))
        
        return largest 