class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        
        def dfs(i: int, prev: int) -> int:
            if i == n:
                return 0
            if (i,prev) in memo:
                return memo[(i,prev)]
            # Option 1: skip nums[i]
            best = dfs(i + 1, prev)

            # Option 2: take nums[i] if it is increasing
            if prev == -1001 or nums[i] > nums[prev]:
                best = max(best, 1 + dfs(i + 1, i))
            memo[(i,prev)] = best 
            return best

        return dfs(0, -1001)