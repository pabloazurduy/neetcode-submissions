class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #1. backtracking: iterate over the array and find the ix for each number in temperatures 
        answ = []
        for i, t in enumerate(temperatures): 
            for k, t2 in enumerate(temperatures[i:]):
                if t2 > t:
                    answ.append(k)
                    break
            if len(answ) <= i: 
                answ.append(0)
        
        return answ

