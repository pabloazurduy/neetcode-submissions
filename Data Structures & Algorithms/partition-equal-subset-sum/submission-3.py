class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_half = sum(nums)/2 # what if its not int ? -> return false 
        def acc_sum(idx:int, target:int) -> bool: 
            if target <0: 
                return False 
            if target > sum(nums[idx:]):
                return False 
            if idx >= len(nums):
                return False 
            if nums[idx] == target:
                return True
             
            return acc_sum(idx+1, target=target-nums[idx]) or acc_sum(idx+1, target=target)
        
        return acc_sum(idx=0, target=nums_half)