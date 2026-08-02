from functools import reduce
from operator import mul
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result:list[int]=[]
        for i in nums:
            nums.remove(i)
            result.append(reduce(mul, nums))
            nums.insert(0,i)
        return result 
        