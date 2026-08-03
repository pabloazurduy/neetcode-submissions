class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        memo:Dict[Tuple[int,int], int] = {}
        def bfs(si:int,ti:int):
            if (si,ti) in memo:
                return memo[(si,ti)]

            #terminal states 
            if si<=len(s) and ti>= len(t):
                memo[(si,ti)] = 1
                return 1 
            elif si >= len(s):
                # if not more elements in s 
                # but not completed then is infeasible
                memo[(si,ti)] = 0
                return 0    
            
            #recursion 
            loc = s[si:].find(t[ti])
            if loc == -1: # not find it the next string
                memo[(si,ti)] = 0
                return 0
            else: # if the next char exist
            # two options
                memo[(si,ti)] = (bfs(si=si+loc+1, ti=ti+1) + # use it 
                                 bfs(si=si+loc+1, ti=ti) # not use it 
                                )
                return memo[(si,ti)]

        
        return bfs(0,0)