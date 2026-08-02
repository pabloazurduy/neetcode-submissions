class Solution:
    


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # I need to search for all the possible subsequences in text1 and see if they are part of tex2 
        # if it is I update the maximum, if not then I move on 
        memo:Dict[Tuple[int, int], int] = {}

        def seq_len(i:int, j:int) -> int:
            if (i,j) in memo:
                return memo[(i,j)]

            if i>=len(text1) or j>=len(text2): # if I arrived to one of the end of the texts
                memo[(i,j)] = 0

            elif text1[i] == text2[j]:
                memo[(i,j)] = 1 + seq_len(i=i+1, j=j+1)
            else: 
                memo[(i,j)] = max(seq_len(i=i, j=j+1), seq_len(i=i+1, j=j))
            
            return memo[(i,j)]


        return seq_len(0,0)
            
            
                                   

        
