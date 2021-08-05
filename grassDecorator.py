from orientationDictionary import OrientationDictionary 
from copy import deepcopy 

class GrassDecorator:
    
    def updateCells(self,matrix,spriteIndexes, createdPath, groundList, defaultSprite):
        spriteDict = OrientationDictionary(spriteIndexes).spriteDict
        tempMatrix = deepcopy(matrix)
        for cell in createdPath:
            cellInfo = [
                [0,0,0],
                [0,1,0],
                [0,0,0]
            ]

            self.fillCellInfo(cellInfo,cell,matrix,3)
            self.updateSprite(cellInfo,spriteDict,cell[0],cell[1],tempMatrix,defaultSprite)
        
        for cell in groundList:
            cellInfo = [
                [0,0,0],
                [0,1,0],
                [0,0,0]
            ]
            self.fillCellInfo(cellInfo,cell,matrix,11)
            self.groundSpriteUpdate(cell,matrix,spriteDict,tempMatrix, cellInfo)
            

        return tempMatrix

    def fillCellInfo(self,cellInfo,cell,matrix, spriteToCheck):
        row , col = cell
        if 0 <= row - 1 < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row-1][col] == spriteToCheck:
            cellInfo[0][1] = 1
            
        if 0 <= row + 1 < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row + 1][col] == spriteToCheck:
            cellInfo[2][1] = 1
        
        if 0 <= row < len(matrix) and 0 <= col + 1 < len(matrix[0]) and matrix[row][col + 1] == spriteToCheck:
            cellInfo[1][2] = 1

        if 0 <= row < len(matrix) and 0 <= col - 1 < len(matrix[0]) and matrix[row][col - 1] == spriteToCheck:
            cellInfo[1][0] = 1
    
    def updateSprite(self,cellInfo,spriteDict,row,column,tempMatrix, defaultSprite):
        found = False
        for spriteInfo in spriteDict:
            if cellInfo in spriteInfo[0]:
                tempMatrix[row][column] = spriteInfo[1]
                found = True

        if not found:
            tempMatrix[row][column] = defaultSprite

    def groundSpriteUpdate(self,cell,matrix,spriteDict,tempMatrix,cellInfo):
        row, column = cell
        leftUpperCorner = [
                    [0,1,0],
                    [1,1,0],
                    [0,0,0]
            ]

        rightUpperCorner = [
                [0,1,0],
                [0,1,1],
                [0,0,0]
            ]

        rightLowerCorner = [
                [0,0,0],
                [0,1,1],
                [0,1,0]
            ]


        leftLowerCorner = [
                [0,0,0],
                [1,1,0],
                [0,1,0]
            ]
                
        if cellInfo == leftUpperCorner:
            if row + 1 < len(matrix) and column + 1 < len(matrix[0]) and matrix[row +1][column - 1] == 3:
                tempMatrix[row + 1][column + 1] = 22
           

        if cellInfo == rightUpperCorner:
            if row + 1 < len(matrix) and 0 <= column - 1 and matrix[row +1][column - 1] == 3:
                tempMatrix[row + 1][column - 1 ] = 20
        

        if cellInfo == rightLowerCorner:
            if 0 <= row - 1 < len(matrix) and 0 <= column - 1 and matrix[row - 1][column - 1] == 3:
                tempMatrix[row - 1][column - 1] = 0
            

        if cellInfo == leftLowerCorner:
            if 0 <= row - 1 < len(matrix) and column + 1 < len(matrix[0]) and matrix[row - 1][column - 1] == 3:
                tempMatrix[row - 1][column + 1] = 2
            


     

        