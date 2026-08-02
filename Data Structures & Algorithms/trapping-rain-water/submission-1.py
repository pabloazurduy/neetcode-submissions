class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        grid = [[None for i in range(len(height))] for j in range(max(height))]
        for h in range(max(height)):
            for c in range(len(height)):
                grid[h][c] = None if height[c]<=h else 'b'
        for row in grid:
            for cc, cell in enumerate(row):
                if cell==None:
                    if row[cc-1]=='w':
                        row[cc]='w'
                        water+=1
                    elif 'b' in row[:cc] and 'b' in row[cc+1:]:         
                        row[cc]='w'
                        water +=1
                    else:
                        continue
        return water