from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    #set to zeros cross shape
                    for ii in range(len(matrix)):
                        if matrix[ii][j] == 0:
                            continue
                        matrix[ii][j] = True

                    for ii in range(len(matrix[i])):
                        if matrix[i][ii] == 0:
                            continue
                        matrix[i][ii] = True
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] is True:
                    matrix[i][j]=0   

# Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]])            
# Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])