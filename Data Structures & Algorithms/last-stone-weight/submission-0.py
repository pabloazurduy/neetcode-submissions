class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while stones and len(stones) >1:
            
            s1 = max(stones)
            stones.remove(s1)
            s2 = max(stones)
            stones.remove(s2)
            print(stones)
            if s1 == s2:
                continue
            elif s1>s2:
                stones.append(s1-s2)

        return stones[0] if stones and len(stones)>0 else 0