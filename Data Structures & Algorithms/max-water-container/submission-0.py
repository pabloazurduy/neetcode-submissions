class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best=0
        for i in range(len(heights)):
            for j in range(i,len(heights)):
                area = (j-i)*min(heights[j],heights[i])
                if area>=best:
                    best=area
        return best

        