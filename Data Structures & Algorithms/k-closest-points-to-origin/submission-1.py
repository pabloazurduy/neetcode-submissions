import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for p in points:
            d = -math.sqrt(p[0]**2+p[1]**2)
            heapq.heappush(max_heap, [d,p[0],p[1]])
            if len(max_heap) > k :
                heapq.heappop(max_heap) # I will get the max 

    
        return [[v[1], v[2]] for v in max_heap ]