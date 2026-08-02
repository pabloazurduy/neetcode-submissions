from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #1. backtracking: iterate over the array and find the ix for each number in temperatures 
        #answ = []
        #for i, t in enumerate(temperatures): 
        #    for k, t2 in enumerate(temperatures[i:]):
        #        if t2 > t:
        #            answ.append(k)
        #            break
        #    if len(answ) <= i: 
        #        answ.append(0)
        #return answ
        
        # 2. better way than n2, using stacks
        ans = [None] * len(temperatures)
        t_stack = deque() # temperatures 
        i_stack = deque() # index of temps 
        for i,t in enumerate(temperatures):
            while len(t_stack)>0 and t > t_stack[-1]:
                t_stack.pop()
                ix = i_stack.pop()
                ans[ix] = i-ix
            t_stack.append(t)
            i_stack.append(i)

        for ix in i_stack:
            ans[ix]=0
        return ans
