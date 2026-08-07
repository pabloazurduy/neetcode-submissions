class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # each element in nums can be in range(len(nums)) positions and the rest as well
        # so all the possible permutations is equal to range(n)*range(n)*range(n)...
        # excluding the repeated positions, so 1,1,1 is not feasible. 
        

        def dperm(nums:List[int]) -> List[List[int]]:
            # base case 
            if nums is None:
                return []
            if len(nums) <= 1:
                return [nums]

            # recursion 
            a = []
            for i in range(len(nums)):
                for subperm in dperm(nums[:i] + nums[i+1:]):
                    a.append([nums[i]]+subperm)     
            return a



        
        return dperm(nums)