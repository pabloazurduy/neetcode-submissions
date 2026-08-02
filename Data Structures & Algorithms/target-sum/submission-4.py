from collections import defaultdict 

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo: Dict[Tuple[int, int], int] = defaultdict(lambda: 0)
        
        def dfs(i:int, target:int)-> None:
            if (i,target) in memo:
                return memo[(i,target)]
            # terminal states 
            if i>=len(nums):
                return 0
            elif i==len(nums)-1:
                if target==nums[i]:
                    memo[(i,target)] +=1 
                if target==-nums[i]:
                    memo[(i,target)] +=1 
                return memo[(i,target)]
            
            # recursion 
            memo[(i,target)] = dfs(i+1, target-nums[i]) +  dfs(i+1, target+nums[i]) 
            return memo[(i,target)]

        return dfs(i=0, target=target)
