class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        memo = {}
        def coins(nums:Tuple[int]) -> int: 
            if nums in memo:
                return memo[nums]
            
            # terminal states
            if len(nums) == 0:
                memo[nums] =0
                return 0 

            # iterative state
            coins_arr = []
            for i in range(len(nums)):
                coins_arr.append(coins(nums[:i] + nums[i + 1:]) 
                                + ((nums[i-1] if i-1 >=0 else 1) *
                                    (nums[i]) *
                                    (nums[i+1] if i+1 < len(nums) else 1))
                                )

            memo[nums] = max(coins_arr) 
            return memo[nums]

        return coins(tuple(nums))