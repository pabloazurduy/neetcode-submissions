from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output:List[int]=[]
        for ix,n in enumerate(nums):
            prod = reduce(lambda a,b: a*b, [k for i,k in enumerate(nums) if i!=ix  ])
            output.append(prod)
        return output