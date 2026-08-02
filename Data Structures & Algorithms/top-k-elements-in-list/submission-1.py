from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts:Dict[int,int] = defaultdict(lambda:0)
        for n in nums: 
            counts[n] +=1 
        pop = sorted(counts.keys(), key= lambda k:counts[k], reverse=True)
        return pop[:k]