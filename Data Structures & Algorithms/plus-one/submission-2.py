from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_s = ''.join([str(d) for d in digits])
        out_n = int(num_s) +1 
        out_l = [int(k) for k in str(out_n)]
        print(out_l)
        return out_l