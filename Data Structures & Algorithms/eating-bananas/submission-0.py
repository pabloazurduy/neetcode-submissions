import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # alternative 1, 
        # assume K in [total_bananas/h, max(piles)] 
        # with that K find if solution is or not feasible 

        total_bananas = sum(piles)
        for k in range(math.ceil(total_bananas/h), max(piles)+1):
            left_h = h 
            for i, p in enumerate(piles):
                left_h -= math.ceil(p/k)
                if left_h < 0:
                    break 
                elif i == len(piles)-1 and left_h>=0:
                    return k

        
        