from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.lineIsValid(row):
                return False
                            
        for col in list(zip(*board[:])):
            if not self.lineIsValid(col):
                return False
  
        for i in range(0,len(board),3):
            for j in range(len(board)//3):
                left,right  = 3*j, (3*j)+3
                submatrix = board[i][left:right] + board[i+1][left:right] + board[i+2][left:right]
                if not self.lineIsValid(submatrix):
                    return False
            
        return True

    def lineIsValid(self, unit: List[str]) -> bool:
        nums = set()        
        for n in range(len(unit)):                        
            if unit[n] in nums:
                return False
            elif unit[n] != '.':
                nums.add(unit[n])
        return True
        

result = Solution().isValidSudoku(
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
)
print(result)

result2 = Solution().isValidSudoku(
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
)
print(result2)