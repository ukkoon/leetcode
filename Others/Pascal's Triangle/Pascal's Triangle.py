from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        col = [[1]]
        for i in range(1,numRows):
            row = [1,1]
            for j in range(1,i):                
                # print(f"[{i}][{j}] = [{i-1}][{j-1}] + [{i-1}][{j}]")
                row.insert(j,col[ i-1 ] [j-1 ] + col[ i-1 ][ j ])                
            col.append(row)
            # print("-----")
        return col