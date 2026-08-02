class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # solution 1, backtracking n2 all possible combinations 
        max_area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                area = (j+1-i) * min(heights[i:j+1])
                print(area, i,j)
                max_area = max(area, max_area)
        return max_area