class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_half = sum(nums)/2 # what if its not int ? -> return false 
        print(nums_half)
        def acc_sum(idx:int, target:int) -> bool: 
            if idx >= len(nums):
                return False 
            if nums[idx] == target:
                return True
            return acc_sum(idx+1, target=target-nums[idx]) or acc_sum(idx+1, target=target)
        
        return acc_sum(idx=0, target=nums_half)