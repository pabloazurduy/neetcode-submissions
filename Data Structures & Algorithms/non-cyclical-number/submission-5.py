from typing import List


class Solution:
    
    
    def isHappy(self, n: int) -> bool:
        self.seen:List[int] = list()
        return self.isHappy_fn(n)
    
    def isHappy_fn(self, n:int) -> bool:
        cycle = sum([int(k)**2 for k in str(n)])
        print(self.seen, cycle)
        if cycle == 1:
            return True # is happy
        elif cycle in self.seen:
            return False # is not happy
        self.seen.append(cycle)
        return self.isHappy_fn(cycle)