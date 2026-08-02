from typing import Dict 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map:Dict[int, int] = {}
        for num in nums:
            hash_map[num] = hash_map.get(num,0) +1 
        if len(hash_map) >0:
            return max(hash_map.values()) >=2 
        else:
            return False 