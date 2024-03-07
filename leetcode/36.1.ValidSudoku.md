class Solution:
    def isUnique(self, arr):
        uniques = set()
        for n in arr:
            if n != '.' and n in uniques:
                return False
            uniques.add(n)
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = []
            col = []
            grid = []
            for j in range(9):
                row.append(board[i][j])
                col.append(board[j][i])
                grid.append(board[3*(i//3) + j//3][3*(i%3) + j%3])
            if (not self.isUnique(row) or
            not self.isUnique(col) or
            not self.isUnique(grid)):
                return False
        return True

# metadata
# relevant-topics array, for loop 
# time-complexity O(1) 47.76%
# space-complexity O(1) 72.15% 
# language python
# difficulty medium
# date 20240307