class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out:List[int] = []
        for i in range(0, len(nums)-k+1):
            out.append(max(nums[i:i+k]))
        return out