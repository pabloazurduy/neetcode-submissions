
import re 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = s[::-1]
        p = p[::-1]

        is_match = False # incumbent 
        memo:Dict[Tuple[int,int]] = {}

        def dfs(i:int,j:int)-> bool:
            
            nonlocal is_match    

            if is_match:
                return True

            # end states
            if j==len(p): # If I finish the pattern 
                if i==len(s): # if I also finished the string
                    is_match = True
                    memo[(i,j)]=True
                    return True
                else:
                    memo[(i,j)]=False
                    return False
            
            if i==len(s) and j<len(p): # if I finish the string and not the pattern
                if re.fullmatch(r"(?:\*[^*])*", p[j:]):
                    memo[(i,j)]=True
                else:
                    memo[(i,j)]=False
                return memo[(i,j)]
                

            # recursion 3 cases 
            paths = []
            # 1. anychar
            if p[j]=='.': 
                paths.append(dfs(i+1,j+1)) # I need to move forward both strings
            #2. specific char 
            elif p[j].isalpha(): 
                if s[i] == p[j]:
                    paths.append(dfs(i+1,j+1)) 
                else:
                    memo[(i,j)]=False
                    return False 
            
            #3. multiplier
            elif p[j] == '*':    
                if p[j+1] == '.':
                    paths.append(dfs(i, j+2)) # don't use and ignore it
                    paths.append(dfs(i+1, j+2)) # use it and finish
                    paths.append(dfs(i+1, j)) # use it and keep it 
                elif p[j+1].isalpha():
                    paths.append(dfs(i, j+2)) # don't use and ignore it
                    if p[j+1] == s[i]:
                        paths.append(dfs(i+1, j+2)) # use it and finish
                        paths.append(dfs(i+1, j)) # use it and keep it 
                
            else:
                raise ValueError(s[i],p[j])
            
            memo[(i,j)]=any(paths)
            #print(memo)
            return memo[(i,j)]
        
        return dfs(0,0)