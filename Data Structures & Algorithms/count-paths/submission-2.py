class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # for each state, the number of paths to arrive to the end state will be the sum of my neighbours ways to arrive to the end state. 
        # we need to find from the origin [0,0] how many ways I have to get to the end, if I'm in the end state will be 0 

        memo:Dict[Tuple[int,int]] = {}
        def paths_to_end(i:int,j:int): 
            if (i,j) in memo:
                return memo[(i,j)]
            if i==n and j==m:
                memo[(i,j)] = 1
            else:
                right_node = 0 if i+1 >n else paths_to_end(i+1,j)
                down_node =  0 if j+1 >m else paths_to_end(i,j+1) 
                memo[(i,j)] = right_node + down_node 
            return memo[(i,j)]
        
        return paths_to_end(1,1) #starting from the origin. 