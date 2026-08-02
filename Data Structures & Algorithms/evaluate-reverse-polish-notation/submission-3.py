from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for char in tokens: 
            if char.lstrip("-").isnumeric():
                stack.append(int(char))
            elif char in ['+', '-', '*', '/']:
                b= stack.pop()
                a= stack.pop()
                stack.append(int(eval(f'{a} {char} {b}')))
        return stack.pop()