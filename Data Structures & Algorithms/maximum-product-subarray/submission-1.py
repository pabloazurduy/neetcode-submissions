class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cmin, cmax = 1,1 
        for n in nums:
            cmin, cmax = min(cmin*n, cmax*n, n),max(cmin*n, cmax*n, n)
            res = max(cmax,cmin,res)
        return res 