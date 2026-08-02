from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        out:List[int] = []
        r=1
        for k in range(len(digits)):
            s = digits[::-1][k] +r
            if s <10 :
                out.append(s)
                r=0
            else:
                out.append(0)
                r=1
        if r==1:
            out.append(1)
        return out[::-1]
