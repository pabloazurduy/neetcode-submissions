class Solution:
    def search(self, nums: List[int], target: int, acc:Optional[int] = 0) -> int:
        mid = len(nums)//2
        if nums[mid] == target:
            return mid + acc 
        elif len(nums) <=1:
            return -1
        if nums[mid] > target:
            return self.search(nums[:mid], target) 
        elif nums[mid] < target: 
            return self.search(nums[mid:], target, acc=mid + acc)
        