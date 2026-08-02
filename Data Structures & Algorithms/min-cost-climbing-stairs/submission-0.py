class Solution:
    def __init__(self):
        self.start = True 

    def minCostClimbingStairs(self, cost: List[int]) -> int: 
        if self.start:
            self.start = False
            print(f'{self.start=}') 
            return min(self.minCostClimbingStairs(cost[0:]) ,
                       self.minCostClimbingStairs(cost[1:]) 
                       )
            
        if len(cost)==0: # base case
            return 0
        else:
            return min(self.minCostClimbingStairs(cost[1:]) ,
                       self.minCostClimbingStairs(cost[2:]) 
                       ) + cost[0]
