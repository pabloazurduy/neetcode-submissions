class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        inc = 0
        def rec(heights:List[int]) -> int:
            nonlocal inc
            lh = len(heights)
            # end states
            if lh == 0:
                return 0 
            if lh==1:
                return heights[0]
            
            if max(heights)*lh < inc: # truncate search tree
                return 0

            mh = min(heights)
            mi = heights.index(mh)
            cr = mh*lh
            inc = max(cr, inc)

            return max([cr, rec(heights[mi+1:]), rec(heights[:mi])])
        
        return rec(heights)