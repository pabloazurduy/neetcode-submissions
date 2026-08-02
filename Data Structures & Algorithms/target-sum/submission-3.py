class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo: Dict[Tuple[int, int], int] = {}
        
        self.total = 0
        def dfs(i:int, target:int) -> int:
            # terminal states 
            if i>=len(nums):
                #memo[(i,target)]=0
                return 
            elif i==len(nums)-1:
                if target==nums[i]:
                    self.total+=1 
                if target==-nums[i]:
                    self.total+=1 
                return  
            
            # recursion 
            dfs(i+1, target-nums[i]) # sum 
            dfs(i+1, target+nums[i]) # substraction
            return 

        dfs(i=0, target=target)
        return self.total

            
            