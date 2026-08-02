from functools import lru_cache
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(i: int, prev: int) -> int:
            if i == n:
                return 0

            # Option 1: skip nums[i]
            best = dfs(i + 1, prev)

            # Option 2: take nums[i] if it is increasing
            if prev == -1001 or nums[i] > nums[prev]:
                best = max(best, 1 + dfs(i + 1, i))

            return best

        return dfs(0, -1001)