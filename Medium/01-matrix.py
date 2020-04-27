'''
https://leetcode.com/problems/01-matrix/
'''
class Solution:
    def dfs(queue):
        while queue:
            row,column,count = queue.pop(0)
            for r,c in ((row,column+1),(row+1,column),(row-1,column),(row,column-1)):
                if (0<=r<totalRows) and (0<=c<totalColumns) and (copyMatrix[r][c]==0):
                    return count+1
                else:
                    queue.append((r,c,count+1))
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        global copyMatrix
        copyMatrix = matrix
        global totalRows
        totalRows=len(matrix)
        for row in range(totalRows):
            global totalColumns
            totalColumns = len(matrix[row])
            for column in range(len(matrix[row])):
                var = matrix[row][column]
                if(var == 0):
                    continue
                found = 0
                for r,c in ((row,column+1),(row+1,column),(row-1,column),(row,column-1)):
                    if (0<=r<totalRows) and (0<=c<totalColumns) and (matrix[r][c]==0):
                        found =1 
                        break
                if(found == 0):
                    count = 0
                    queue = [(row,column,count)]
                    copyMatrix[row][column]=Solution.dfs(queue)
        return copyMatrix