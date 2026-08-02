class Solution:
    def checkSet(self, num_set:List[str]) -> bool:
        digits = [str(n) for n in range(1,10)]
        for digit in num_set:
            if digit == '.':
                pass 
            else:
                if digit in digits:
                    digits.remove(digit)
                else:
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #generate sets 
        columns:Dict[int,str] = {}
        cells:Dict[Tuple[int,int],str]={}
        for i,row in enumerate(board):
            for j, digit in enumerate(row):
                #col
                col = columns.get(j, []) 
                col.append(digit)
                columns[j] = col
                #cell
                cell = cells.get((i//3,j//3), [])
                cell.append(digit)
                cells[(i//3,j//3)] = cell 
        # row check 
        for row in board:
            if self.checkSet(row) == False:
                return False
        # col check
        for col in columns.values():
            if self.checkSet(col) == False:
                return False    
        # cell check
        for cell in cells.values():
            if self.checkSet(cell) == False:
                return False    
        return True



