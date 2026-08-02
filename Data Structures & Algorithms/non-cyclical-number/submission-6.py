from typing import List


class Solution:
    def __init__(self):
        self.seen: List[int] = []
    
    def isHappy(self, n: int) -> bool:
        cycle = sum([int(k)**2 for k in str(n)])
        print(self.seen, cycle)
        if cycle == 1:
            return True  # is happy
        elif cycle in self.seen:
            return False  # is not happy
        self.seen.append(cycle)
        return self.isHappy(cycle)