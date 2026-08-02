class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s_nums = list(sorted(set(nums)))
        if len(s_nums)==1:
            return 1
        longest = 0
        inc = 1
        for i, n in enumerate(s_nums[1:]):
            print(inc,n,s_nums[i]+1,s_nums)
            if n==1+s_nums[i]:
                inc+=1 
            else:
                inc=1
            if inc>longest:
                longest=inc
        return longest 
