from collections import deque

par_dict = {'(':')',
            '{':'}', 
            '[':']'}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque() 
        for char in s:
            if char in par_dict.keys():
                stack.append(char)     
            elif char in par_dict.values():
                try:       
                    next_p = stack.pop()
                except IndexError:
                    return False
                if char != par_dict[next_p]:
                    return False 
        return len(stack) == 0
    