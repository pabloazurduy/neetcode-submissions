class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo:Dict[Tuple[int,bool], int] = {}

        def profit(t:int, coin:bool)->int:
            if (t,coin) in memo:
                return memo[(t,coin)]

            if t>=len(prices):
                return 0
            memo[(t,coin)] = max( profit(t+1, coin), # do nothing 
                        profit(t+1, coin =True) - prices[t] if coin==False else 0 ,# buy if I don't have a coin 
                        profit(t+2, coin =False) + prices[t] if coin==True else 0 # sell if I do have a coin
            )
            return memo[(t,coin)]
        return profit(0,False)