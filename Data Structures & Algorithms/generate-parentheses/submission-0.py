from typing import Any
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # alternative 1, try all combinations of 2*n parethnesis, validate if they are "valid" and return
        # is there an smarter way of doing the same ?
        # recursive way ? 
        solution = []
        def pstack(current_stack:Any, left_to_open:int):
            left_to_close = 0
            for c in current_stack:
                if c == '(':
                    left_to_close +=1 
                elif c ==  ')':
                    left_to_close -=1 
            # base case 
            if left_to_open == 0 and left_to_close == 0:
                solution.append(''.join(current_stack))
            
            if left_to_open >=1:
                stack = current_stack + ['(']
                pstack(stack, left_to_open-1)          
            if left_to_close >=1:
                stack = current_stack + [')']  
                pstack(stack, left_to_open)

        pstack(current_stack = [], left_to_open=n)
        return solution 
