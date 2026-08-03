class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = {}
        def dfs(i,j) -> int:
            if (i,j) in memo:
                return memo[(i,j)]

            # terminal states 
            if j==len(word2): # this is a terminal state 
                #two options: 1, I still have some elements to remove from word1, 2 I don't 
                memo[(i,j)] = len(word1)-i # how many remining chars do I have on word1. 
                return memo[(i,j)]
            if i==len(word1): # this is also a terminal state
                memo[(i,j)] = len(word2)-j # I need to add the remaining chars
                return memo[(i,j)]

            if word1[i] == word2[j]: # if equal then keep going 
                memo[(i,j)] = dfs(i+1,j+1) # move forward 
                return memo[(i,j)]
            else: # if not equal then I can add or delete 
                shortest= min(  # replace one char
                                dfs(i+1,j+1) +1, 
                                # insert one char   
                                dfs(i,j+1)+1 if j+1<len(word2) else 101, 
                                # delete one char 
                                dfs(i+1,j)+1 if i+1<len(word1) else 101,  
                            )
                memo[(i,j)] = shortest
                return shortest

        return dfs(0,0)


