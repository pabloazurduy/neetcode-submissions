class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo:Dict[Tuple[int,bool], int] = {}
        def rd(i:int, rob_0:bool=False)-> int:
            print(memo)
            if (i,rob_0) in memo:
                return memo[(i,rob_0)]
            # end state 
            if (rob_0 and i>=len(nums)-1) or (not rob_0 and i>=len(nums)):
                memo[(i, rob_0)] = 0
                return 0

            # iter 
            if i >0:
                val = max(rd(i+1, rob_0), 
                        nums[i]+ rd(i+2, rob_0) 
                        )
            elif i==0:
                val = max(rd(i+1, rob_0=False), # I do not rob the origin
                          nums[i] + rd(i+2, rob_0=True) # I rob the origin 
                        )

            memo[(i,rob_0)] = val
            return val
        
        return rd(0)
