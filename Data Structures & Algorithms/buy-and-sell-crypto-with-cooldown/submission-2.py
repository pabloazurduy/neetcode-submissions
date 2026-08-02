class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo:Dict[Tuple[int,bool,int], int] = {}

        def profit(t:int, coin:bool, amt:int)->int:
            if (t,coin,amt) in memo:
                return memo[(t,coin,amt)]
            
            if t>=len(prices):
                memo[(t,coin,amt)] = amt
                return memo[(t,coin,amt)]
            if coin:
                memo[(t,coin,amt)] = max(profit(t+1, coin=True, amt = amt), # not sell
                           profit(t+2, coin=False, amt= amt+prices[t]) # sell + skip one period
                        )
            else:
                memo[(t,coin,amt)] =  max (profit(t+1, coin=False, amt=amt), #not buy 
                            profit(t+1, coin=True, amt=amt-prices[t]) 
                )
            
            return memo[(t,coin,amt)]

        return profit(t=0, coin=False, amt=0)
