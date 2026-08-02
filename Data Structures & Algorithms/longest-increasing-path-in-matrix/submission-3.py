from itertools import product
from random import shuffle
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        memo:Dict[Tuple[int,int], int] = {}
        y = len(matrix)
        x = len(matrix[0])
        def path_ahead(i:int,j:int)-> int:
            if (i,j) in memo:
                return memo[(i,j)]

            next_s = [(i+t1,j+t2) for (t1, t2) in [(-1,0), (1,0), (0,1), (0,-1)] if x>i+t1>=0 and y>j+t2>=0 and matrix[j+t2][i+t1]> matrix[j][i]]

            if len(next_s)==0:
                memo[(i,j)] =1# terminal state 
            else:
                memo[(i,j)] = max([path_ahead(s[0], s[1]) for s in next_s])+1
            return memo[(i,j)]
        

        coords = list(product(range(x), range(y)))
        coords = sorted(coords, key = lambda s: matrix[s[1]][s[0]], reverse=True)
        for i,j in coords:
            path_ahead(i,j)
        
        return max(memo.values())


