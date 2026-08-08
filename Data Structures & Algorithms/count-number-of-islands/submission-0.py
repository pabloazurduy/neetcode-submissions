from itertools import product 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        seen:Set[Tuple[int, int]] = set()
        def dfs(i:int,j:int) -> None:
            nonlocal seen
            if (i,j) in seen: # already visited
                return 
            if i>=len(grid) or j>=len(grid[0]) or j<0 or i<0: #border
                return
            if grid[i][j] == '0': # if water
                return
            if grid[i][j] == '1': # if land
                seen.add((i,j)) 
                for u,v in [(1,0), (0,1), (-1,0), (0,-1)]:
                    dfs(i+u,j+v)
        
        num_islands = 0
        for (i,j) in product(range(len(grid)), range(len(grid[0]))):
            if (i,j) not in seen and grid[i][j] == '1':
                num_islands += 1
                dfs(i,j)
            else:
                seen.add((i,j)) # add also waters ? -do I need?-

        return num_islands