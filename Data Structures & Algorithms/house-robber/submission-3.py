
class Solution:
    def __init__(self):
        self.cache = {'[]':0}
    def rob(self, nums: List[int]) -> int:
        if str(nums) in self.cache:
            return self.cache[str(nums)]
        else:
            maxv= max(self.rob(nums[1:]), # skip current house 
                       self.rob(nums[2:])+ nums[0] # rob current house and skip next one
                       )
            self.cache[str(nums)]=maxv
            return maxv 