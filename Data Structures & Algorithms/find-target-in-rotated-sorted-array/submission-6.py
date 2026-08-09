class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        def msearch(i: int, j:int) -> int:
            print(i,j)
            if i==j or j-i==1:
                if nums[i]==target:
                    return i
                elif nums[j]==target:
                    return j
                else:
                    return -1

            
            m = (i+j)//2
            # right side 
            if ((nums[m]<= nums[j] and  nums[m] <= target and target <= nums[j]) or # sorted 
                (nums[m]>= nums[j] and (nums[m] <= target or  nums[j] >= target))): # unsorted 
                return msearch(m, j)
            # left side 
            if ((nums[i] <= nums[m] and nums[i] <= target and target <= nums[m]) or # sorted
               (nums[i] >= nums[m]  and (nums[m] >= target or nums[i] <= target))): # unsorted
                return msearch(i, m)
    
            return -1 
        return msearch(0,len(nums)-1)
            